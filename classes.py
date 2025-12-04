class textGeneratedContent:

    def __init__(self, height, body_shape, skintone, undertone):
        self.height = height
        self.body_shape = body_shape
        self.skintone = skintone
        self.undertone = undertone

    def HeightAndBodyReason(self, height, body_shape):
        self.height = height
        self.body_shape = body_shape

        reasonPrompt = f"""Combining these two features, reason about the aesthetics and physicality of both features in terms
        of the outfit to be recommended {self.height} & {self.body_shape} Make sure that you generate less but concise information, aim for efficiency and effectiveness"""
    
        return reasonPrompt

    def SkintoneAndUndertoneReason(self, skintone, undertone):
        self.skintone = skintone
        self.undertone = undertone

        reasonPrompt = f"""Combining these two features, reason about the aesthetics and physicality of both features in terms
        of the outfit to be recommended {self.skintone} & {self.undertone} Make sure that you generate less but concise information, aim for efficiency and effectiveness"""

        return reasonPrompt

    def FeatureCombinationReason(self, firstCombination, secondCombination):
        self.firstCombination = firstCombination
        self.secondCombination = secondCombination

        reasonPrompt = f"""These are the generated output from you, the same model, the goal here is to combine the two combinations to 
        come about a recommendation of outfit, here they are {firstCombination} & {secondCombination}"""

        return reasonPrompt