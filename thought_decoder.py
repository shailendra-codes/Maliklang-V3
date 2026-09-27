import numpy as np

class ThoughtDecoder:
    def __init__(self):
        # Neural intention mapping dictionary for healthcare assistance
        self.intent_matrix = {
            "high_beta_spike": "Emergency - Severe Pain Detected",
            "stable_beta_cluster": "Patient Requesting Water",
            "alpha_dominant": "Patient is Calm and Resting",
            "theta_rhythm": "Patient is Drowsy / Sleeping",
            "delta_surge": "Warning - Deep Coma or Low Brain Activity"
        }

    def decode_neural_zones(self, cleaned_matrix: dict) -> dict:
        """
        Processes cleaned channels and classifies brain activity into 3 distinct zones.
        """
        decoded_output = {
            "zone": "Unknown",
            "detected_intent": "Analyzing Brainwaves...",
            "confidence_score": 0.0
        }
       
        all_amplitudes = []
        for channel, signal in cleaned_matrix.items():
            all_amplitudes.extend(signal)
           
        if not all_amplitudes:
            return decoded_output
           
        mean_amp = np.mean(np.abs(all_amplitudes))
       
        # Classification into 3 custom neuro-signal zones
        if mean_amp > 60.0:
            decoded_output["zone"] = "Active Zone (Red)"
            decoded_output["detected_intent"] = self.intent_matrix["high_beta_spike"]
            decoded_output["confidence_score"] = float(np.round(min(99.4, mean_amp * 1.2), 2))
        elif 15.0 <= mean_amp <= 60.0:
            decoded_output["zone"] = "Relax Zone (Green)"
            decoded_output["detected_intent"] = self.intent_matrix["alpha_dominant"]
            decoded_output["confidence_score"] = float(np.round(min(95.0, mean_amp * 1.5), 2))
        else:
            decoded_output["zone"] = "Deep Zone (Blue)"
            decoded_output["detected_intent"] = self.intent_matrix["delta_surge"]
            decoded_output["confidence_score"] = float(np.round(min(98.9, (100 - mean_amp)), 2))
           
        return decoded_output
 
