import logging

class ContentValidator:
    def __init__(self):
        self.hard_rules = [
            "주식 배제",
            "12차원 사고 준수",
            "의장님 철학 유지"
        ]

    def validate(self, content_metadata: dict) -> bool:
        """
        Validates the content against NR_014.
        In a real scenario, this would use an LLM to check the script/title.
        """
        title = content_metadata.get('title', '')
        description = content_metadata.get('description', '')
        
        # Simple keyword check for 'stock' (주식) as a placeholder
        forbidden_keywords = ["주식", "상한가", "급등주"]
        for kw in forbidden_keywords:
            if kw in title or kw in description:
                logging.warning(f"NR_014 Violation: Forbidden keyword '{kw}' found.")
                return False
        
        # Placeholder for 12-dimensional thinking check
        # This would require more sophisticated NLP
        return True
