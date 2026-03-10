# 👗 AI Personal Shopper & Stylist

A multi-stage AI pipeline that provides personalized fashion recommendations. By combining **Body Geometry Analysis**, **Color Theory**, and **Live Web Search**, this tool acts as a professional stylist to curate real-world outfits tailored to a user's unique physical traits.

## 🚀 How It Works
The system follows a three-step reasoning chain using Google's Gemini 2.5 models:

1.  **Geometric Analysis:** Analyzes height and body shape to define "Golden Rules" for silhouettes and cuts.
2.  **Color Analysis:** Evaluates skin tone and undertones to build a custom color palette of "Power Colors" and "Neutrals."
3.  **The Personal Shopper:** Merges the rules and colors. It then utilizes **Google Search Grounding** to find actual products currently available at retailers like Uniqlo, Zara, and H&M.

## ✨ Key Features
* **Chained LLM Reasoning:** Uses separate specialized prompts for body shape and color theory before final synthesis.
* **Google Search Integration:** Unlike standard AI, this tool searches the live web to ensure recommended items actually exist.
* **Visual Mock-up Generation:** Provides a detailed prompt at the end of every recommendation designed for text-to-image generators (like Midjourney or DALL-E).
* **Cross-Model Synergy:** Uses `Gemini-2.5-Flash` for fast initial analysis and `Gemini-2.5-Pro` for high-level reasoning and search-based shopping.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **AI Models:** Google Gemini 2.5 Flash & Pro
* **Tools:** Google Gen AI SDK, Google Search Tooling
* **Libraries:** `PIL`, `google-genai`

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ajlrza/ai-personal-shopper.git](https://github.com/ajlrza/ai-personal-shopper.git)
   cd ai-personal-shopper
   ```

2. **Install dependencies:**
   ```bash
   pip install -U google-genai pillow
   ```

3. **Configure API Key:**
   Set your Google AI Studio API key in the script:
   ```python
   client = genai.Client(api_key="YOUR_API_KEY")
   ```

4. **Run the Stylist:**
   ```bash
   python main.py
   ```

## 📋 Usage Example
Input your details when prompted:
* **Sex:** Male/Female/Non-binary
* **Height:** e.g., 5'11"
* **Body Shape:** e.g., Athletic, Inverted Triangle, Pear
* **Skin Tone:** e.g., Deep, Olive, Fair
* **Undertone:** e.g., Cool, Warm, Neutral

The AI will output 3 complete outfit combinations (Casual, Work, Date Night) with specific search queries to buy the items.

---
*Note: This project was developed as an exploration of Agentic Workflows and Tool-Use (Function Calling) within the Google Gemini ecosystem.*
