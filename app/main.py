"""Local synthetic demo service; uploaded bytes are never persisted."""

import base64
import binascii
import os
import time
from dataclasses import asdict

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from quality_inspection.baseline import MAX_IMAGE_BYTES
from quality_inspection.demo import demo_model, synthetic_image

MAX_REQUEST_BYTES = 7 * 1024 * 1024
app = FastAPI(title="Manufacturing Quality Inspection — Synthetic Demo", version="0.1.0")
model = demo_model()


@app.middleware("http")
async def bound_request(request: Request, call_next):
    if request.url.path == "/inspect" and request.method == "POST":
        length = request.headers.get("content-length")
        if length is not None:
            try:
                if int(length) < 0 or int(length) > MAX_REQUEST_BYTES:
                    raise ValueError
            except ValueError:
                return HTMLResponse("Request too large or invalid length", status_code=413)
        # Count actual streamed bytes too; a client may omit or lie about content-length.
        chunks = []
        size = 0
        async for chunk in request.stream():
            size += len(chunk)
            if size > MAX_REQUEST_BYTES:
                return HTMLResponse("Request exceeds 7 MiB", status_code=413)
            chunks.append(chunk)
        request._body = b"".join(chunks)
    return await call_next(request)


class InspectRequest(BaseModel):
    image_base64: str = Field(min_length=1, max_length=7_000_000)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "model_source": model.source, "runtime_llm_tokens": 0}


@app.post("/inspect")
def inspect(payload: InspectRequest) -> dict:
    start = time.perf_counter()
    try:
        raw = base64.b64decode(payload.image_base64, validate=True)
        if len(raw) > MAX_IMAGE_BYTES:
            raise ValueError("Image exceeds 5 MiB")
        result = model.inspect(raw)
    except (ValueError, binascii.Error) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return {
        **asdict(result),
        "latency_ms": (time.perf_counter() - start) * 1000,
        "runtime_llm_tokens": 0,
        "warning": "Synthetic demo model. Operator review required; no automatic product release.",
    }


@app.get("/samples/{kind}")
def sample(kind: str) -> dict:
    if kind not in {"healthy", "defect"}:
        raise HTTPException(status_code=404, detail="Unknown sample")
    return {
        "image_base64": base64.b64encode(
            synthetic_image(900 if kind == "healthy" else 901, defective=kind == "defect")
        ).decode()
    }


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return """<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quality Inspection Demo</title>
<style>
body{font:16px system-ui;background:#f3f5f7;color:#152432;
max-width:780px;margin:6vh auto;padding:24px}
main{background:white;padding:32px;border-radius:16px}button{padding:12px;margin:8px 4px 8px 0}
pre{white-space:pre-wrap;background:#eef2f6;padding:16px}img{width:192px;image-rendering:pixelated}
aside{border-left:4px solid #cc8b22;padding:12px;background:#fff5df}
label{display:block;margin-top:20px}
</style><main><p>MANUFACTURING / QUALITY TRIAGE</p><h1>Image inspection workbench</h1>
<aside>This model uses synthetic images. Results demonstrate a workflow and cannot certify products.
Every product still needs an operator decision.</aside>
<p>Try a healthy bottle or a visible defect, then inspect a local PNG/JPEG.
Uploads stay in memory and are not stored.</p>
<button onclick="example('healthy')">Healthy sample</button>
<button onclick="example('defect')">Defect sample</button>
<label>Upload PNG/JPEG (up to 5 MiB)
<input type="file" id="file" accept="image/png,image/jpeg"></label>
<p><img id="preview" alt="Selected inspection image" hidden></p>
<pre id="result" aria-live="polite">Choose a sample to begin.</pre>
<p>Runtime LLM/VLM API calls: 0. API reference: <a href="/docs">/docs</a></p></main>
<script>
async function run(value){
 document.querySelector('#preview').src='data:image/png;base64,'+value;
 document.querySelector('#preview').hidden=false;
 try{
 const response=await fetch('/inspect',{method:'POST',headers:{'Content-Type':'application/json'},
 body:JSON.stringify({image_base64:value})});
 document.querySelector('#result').textContent=JSON.stringify(await response.json(),null,2);
 }catch(error){document.querySelector('#result').textContent='Request failed: '+error.message;}
}
async function example(kind){
 const response=await fetch('/samples/'+kind);await run((await response.json()).image_base64);
}
document.querySelector('#file').addEventListener('change',event=>{
 const file=event.target.files[0];if(!file)return;
 if(file.size>5*1024*1024){
 document.querySelector('#result').textContent='File exceeds 5 MiB';return;}
 const reader=new FileReader();reader.onload=()=>run(reader.result.split(',')[1]);
 reader.readAsDataURL(file);
});
</script></html>"""


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=os.getenv("MQI_HOST", "127.0.0.1"),
        port=int(os.getenv("MQI_PORT", "8000")),
    )
