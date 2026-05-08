# CHON: JOS-1000B Alpha Autonomous Growth System

5대 자율 집행 및 감시 에이전트 체계의 중추 시스템입니다.

## 에이전트 구성
1. **Alpha-Creator (집행)**: 콘텐츠 생산 및 사출
2. **Sentinel-Verifier (감시)**: 무결성 검증 및 규정 준수
3. **Catalyst-Learner (성장)**: 비즈니스 모델 학습 및 진화
4. **Auditor-Cash (재무)**: 수익 및 리스크 관리
5. **Nexus-Commander (통제)**: 데이터 취합 및 정본 리포트 사출

## 실행 방법
### 통합 리포트 생성
```bash
python3 src/integration/report_manager.py
```

## 보고 체계
모든 에이전트는 `/home/team/shared/REPORTS.md`에 정의된 규약에 따라 작업 결과를 보고해야 합니다.
Nexus-Commander는 해당 데이터를 취합하여 매일 아침 의장님께 [정본 리포트]를 사출합니다.
