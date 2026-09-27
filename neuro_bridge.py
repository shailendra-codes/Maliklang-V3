import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from neuro_demodulator import NeuroDemodulator
from neuro_crypt import NeuroCrypt
from thought_decoder import ThoughtDecoder

app = FastAPI(title="Maliklang-V3 Neuro-AI Bridge")

# Initialize our core independent engines
demodulator = NeuroDemodulator(sample_rate=256)
crypto = NeuroCrypt()
decoder = ThoughtDecoder()

class RawBrainwaveInput(BaseModel):
    raw_signals: dict  # Format: {"channel_1": [12.4, -45.2, ...]}

@app.get("/")
async def root():
    return {"status": "online", "system": "Maliklang-V3", "mode": "Independent Offline Neuro-AI"}

@app.post("/process-brainwaves")
async def process_brainwaves(payload: RawBrainwaveInput):
    try:
        # Step 1: Clean raw EEG channels from motion/muscle noise matrix
        cleaned = demodulator.clean_signal(payload.raw_signals)
       
        # Convert to JSON string for safety encryption block
        cleaned_json = json.dumps(cleaned)
       
        # Step 2: Encrypt data instantly using memory-transient keys
        encrypted_data = crypto.encrypt_neural_matrix(cleaned_json)
       
        # Step 3: Temporarily decrypt strictly inside the inference vault
        secure_vault_str = crypto.decrypt_for_inference(encrypted_data)
        secure_matrix = json.loads(secure_vault_str)
       
        # Step 4: AI Engine ডিকোডিং into 3 distinct diagnostic zones
        diagnostic_result = decoder.decode_neural_zones(secure_matrix)
       
        # Step 5: Hard volatile RAM wipe to destroy raw traces instantly
        crypto.hard_volatile_wipe(cleaned, cleaned_json, secure_vault_str, secure_matrix)
       
        return {
            "success": True,
            "neuro_signal_analysis": diagnostic_result
        }
       
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Neural Pipeline Error: {str(e)}")
 
