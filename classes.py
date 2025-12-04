class textGeneratedContent:

    def __init__(self, height, body_shape, skintone, undertone):
        self.height = height
        self.body_shape = body_shape
        self.skintone = skintone
        self.undertone = undertone

    def HeightAndBodyReason(self, sex, height, body_shape):
        # We update self variables to ensure they are current
        self.sex = sex
        self.height = height
        self.body_shape = body_shape

        # NEW: We ask for specific "Style Rules" rather than just general reasoning.
        reasonPrompt = f"""
        Act as a fashion stylist. 
        Analyze a user with Height: {self.height} and Body Shape: {self.body_shape} along with their sex: {self.sex}.
        
        Output a concise list of "Golden Rules" for this body type:
        1. What specific clothing cuts visually balance their proportions?
        2. What silhouettes should they strictly avoid?
        3. Explain the geometry of why these work.
        """
        return reasonPrompt

    def SkintoneAndUndertoneReason(self, skintone, undertone):
        self.skintone = skintone
        self.undertone = undertone

        # NEW: We ask for specific colors to "Search For" later.
        reasonPrompt = f"""
        Act as a color analysis expert.
        Analyze a user with Skin Tone: {self.skintone} and Undertone: {self.undertone}.
        
        Output a concise color palette:
        1. "Power Colors" (Top 3 specific color names that make them glow).
        2. "Neutrals" (Best colors for basics like coats/trousers).
        3. "Avoid" (Colors that will wash them out).
        """
        return reasonPrompt

    def FeatureCombinationReason(self, firstCombination, secondCombination):
        # CRITICAL FIX: We must extract .text from the response objects
        # If the user passed the full object, we try to access .text. 
        # If they passed a string, we use it as is.
        
        text1 = getattr(firstCombination, 'text', str(firstCombination))
        text2 = getattr(secondCombination, 'text', str(secondCombination))

        # NEW: The "Personal Shopper" Prompt
        reasonPrompt = f"""
        You are an AI Personal Shopper equipped with Google Search.
        
        Review the Style Rules:
        {text1}
        
        Review the Color Palette:
        {text2}
        
        Based on these combined constraints, create 3 Complete Outfits (Casual, Work, Date Night).
        
        For EVERY item in the outfit, provide:
        1. **The Item Name:** (e.g. "High-waisted Wide Leg Trousers in Charcoal")
        2. **Why it works:** Short sentence linking back to the body shape/color analysis.
        3. **Search Query:** A specific string I can copy-paste to find this exact item (e.g. "Zara women wide leg charcoal trousers high waist").
        
        **VISUAL MOCK-UP PROMPT:**
        At the end of the response, write a single, detailed text description of the best outfit that I can paste into an image generator to see what it looks like.
        """

        return reasonPrompt