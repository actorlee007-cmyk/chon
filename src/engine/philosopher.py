
# src/engine/philosopher.py

class ChairmanPhilosophy:
    """
    의장님의 철학 (정본 궤도, 주식 배제, 12차원 사고)
    """
    RULES = [
        "정본 궤도: 본질적이고 올바른 가치를 지향한다.",
        "주식 배제: 단순한 투기나 주식 차익 실현 목적의 정보는 배제한다.",
        "12차원 사고: 다각적이고 깊이 있는 통찰을 추구한다. 표면적인 트렌드 너머의 본질을 본다."
    ]

    @classmethod
    def apply_philosophy(cls, trend_data: str) -> str:
        # 이 부분은 나중에 LLM을 사용하여 고도화할 예정
        # 현재는 규칙을 명시하는 용도로 사용
        return f"Combining trend with philosophy: {trend_data}"

    @classmethod
    def is_aligned(cls, trend_text: str) -> bool:
        # 주식 관련 키워드가 포함되어 있으면 부적합 판정
        stock_keywords = ["stock", "주식", "매수", "매도", "나스닥", "코스피", "dividend", "주가"]
        for keyword in stock_keywords:
            if keyword.lower() in trend_text.lower():
                return False
        return True
