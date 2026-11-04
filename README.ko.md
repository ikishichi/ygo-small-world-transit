# ygo-small-world-transit

[유희왕 스몰 월드 경로 검색](https://ygo-small-world-transit.streamlit.app/?lang=ko)은 [유희왕 뉴런](https://www.db.yugioh-card.com/yugiohdb/?request_locale=ko)의 공개 덱 URL에서 [**스몰 월드**](https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=16555&request_locale=ko) 서치 경로를 찾는 앱입니다.

<div align="center">

[日本語](README.md) | [English](README.en.md) | **한국어** | [简体中文](README.zh-CN.md)

</div>

## 사용 방법

YouTube에서 [사용 방법 동영상](https://www.youtube.com/watch?v=VVvS8u706BM&t=6s)을 볼 수 있습니다.

1. 덱 페이지 상단에 표시된 공개 덱 URL을 입력하고 **덱 불러오기**를 누르거나, 첫 화면에서 **샘플로 체험**을 누릅니다.
2. 패에서 공개할 몬스터를 선택합니다. 서치할 몬스터는 선택 사항입니다. 비워 두면 불러온 덱에서 도달할 수 있는 모든 서치 대상을 찾습니다.
3. **경로 검색**을 누릅니다. 결과는 서치 대상별로 표시됩니다. **경유 몬스터순**을 선택하면 경유 몬스터별로 묶어 볼 수 있습니다.
4. **일치 항목 보기**를 열면 패 → 경유 카드 → 서치 대상 경로와 각 단계에서 일치한 항목을 확인할 수 있습니다.

덱을 불러온 뒤 **덱 변경**을 눌러 URL 입력란을 열면 다른 덱을 불러오거나 현재 덱을 다시 불러올 수 있습니다. 불러온 뒤 페이지를 북마크하면 다음에도 같은 덱을 불러옵니다. 검색 선택과 결과는 저장되지 않습니다.

## 언어

[日本語](https://ygo-small-world-transit.streamlit.app/?lang=ja) / [English](https://ygo-small-world-transit.streamlit.app/?lang=en) / [한국어](https://ygo-small-world-transit.streamlit.app/?lang=ko) / [简体中文](https://ygo-small-world-transit.streamlit.app/?lang=zh-CN)

기본 표시 언어는 일본어입니다. 앱 제목 위의 지구본 메뉴에서 표시 언어를 바꿀 수 있습니다. 화면 표시 언어와 덱 정보 언어는 서로 독립적입니다. `request_locale`이 지정되어 있으면 해당 언어로 덱 정보를 가져오고, 지정되지 않으면 화면 표시 언어를 사용합니다. 간체 중국어의 DB 언어 코드는 `cn`입니다.

## 로컬 실행

Python 3.12 이상이 필요합니다.

1. 이 저장소를 clone한 뒤 프로젝트 루트로 이동합니다.
2. 필요한 패키지를 설치합니다.

   ```bash
   python -m pip install -r requirements.txt
   ```

3. 앱을 실행합니다.

   ```bash
   python -m streamlit run ./src/ui.py
   ```

다른 Python 프로젝트와 패키지 충돌을 피하려면 가상 환경을 사용하세요. `streamlit` 명령을 찾을 수 없으면 `python -m streamlit`로 실행하세요. `No module named streamlit` 오류가 표시되면 앱 실행에 사용하는 Python으로 요구 패키지를 설치하세요.

## 개발

테스트는 프로젝트 루트에서 실행합니다.

```bash
python -m pytest
```

요구 사항과 구조는 [설계 문서](docs/ygo-small-world-transit.md)를 참고하세요.

### 의존성 관리

의존성은 `requirements.in`에서 관리합니다. `requirements.txt`는 직접 및 간접 의존성 버전을 고정한 생성 파일입니다. 두 파일을 모두 커밋하고 설치에는 `requirements.txt`를 사용합니다. 생성 도구 `uv`의 버전은 `requirements-tools.txt`에 고정되어 있습니다.

```bash
python -m pip install -r requirements-tools.txt
python -m uv pip compile requirements.in --output-file requirements.txt
```

의존성을 변경할 때는 `requirements.in`을 수정하고 `requirements.txt`를 다시 생성하세요. 생성 파일을 직접 수정하지 마세요. 지정 범위 안에서 패키지 하나를 업데이트하려면 `--upgrade-package PACKAGE`, 전체 패키지를 업데이트하려면 `--upgrade`를 추가합니다.

```bash
python -m uv pip compile requirements.in --output-file requirements.txt --upgrade-package streamlit
python -m uv pip compile requirements.in --output-file requirements.txt --upgrade
```

CI는 테스트 전에 잠금 파일 재생성으로 변경 사항이 생기지 않는지 확인합니다.

### 의존성 보안 검사

[Dependency security 워크플로](https://github.com/ikishichi/ygo-small-world-transit/actions/workflows/dependency-security.yml)는 매주 토요일과 `main` 대상 PR이 생성·업데이트·재개될 때 Trivy로 `requirements.txt`를 검사합니다. Actions 화면에서 수동 실행할 수도 있습니다. 제외 설정 적용 후 High 또는 Critical 취약점이 남거나, DB 다운로드에 실패하거나, 보고서 또는 제외 설정이 잘못된 경우 검사가 실패합니다. 수정 버전이 아직 공개되지 않은 취약점도 검사 대상입니다.

워크플로 Summary에서 탐지·임시 제외·판정 대상 건수와 검사 실패 기준인 High·Critical 목록, 제외 사유 및 만료일을 확인할 수 있습니다. DB 다운로드 실패, 보고서 누락·손상, 제외 설정 오류, Trivy가 고정 패키지를 누락한 경우에도 검사 오류로 처리됩니다. `dependency-security-report` 아티팩트에는 제외 전·후 JSON 보고서, Summary, 검사한 고정 파일, 제외 설정이 14일간 보관됩니다. 취약점을 임시 제외하려면 `.trivyignore`에 ID를 추가하고, 수정 버전으로 업그레이드한 뒤 제외 항목을 삭제하세요. 제외 전 탐지 결과는 원본 JSON에 남습니다.

## 호스팅 앱 절전 방지

[Keep Streamlit app awake 워크플로](https://github.com/ikishichi/ygo-small-world-transit/actions/workflows/keep_alive.yml)는 3시간마다 Playwright Chromium으로 호스팅 앱을 엽니다. 브라우저 언어는 `ja-JP`로 고정됩니다. 절전 화면이 표시되면 해제하고 제목, 편집 가능한 덱 URL 입력란, 활성화된 **デッキ取得** 버튼이 나타나는지 확인합니다. 덱을 불러오거나 검색하지 않습니다. 이 정기 실행은 포크 저장소에서 실행되지 않습니다.

### 복구 확인 및 실패 대응

복구를 최대 120초 기다리고 한 번 재시도합니다. 각 페이지 이동 대기는 별도로 최대 30초입니다. 복구를 확인하지 못하면 워크플로가 실패하며, 스크린샷과 각 iframe의 HTML이 아티팩트에 7일간 보관됩니다. 로그와 아티팩트에서 네트워크 장애, Streamlit 장애, 페이지나 버튼 변경을 확인하세요. 이 검사는 화면만 확인하며 덱 불러오기와 검색 기능을 검증하지 않습니다.

GitHub [예약 실행](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)은 지연되거나 누락될 수 있으며, 공개 저장소에서 60일간 활동이 없으면 자동으로 비활성화됩니다. 필요한 경우 Actions 화면에서 다시 활성화하세요. [Streamlit Community Cloud의 절전 조건](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#app-hibernation)과 화면은 바뀔 수 있으므로 항상 접속 가능하다고 보장하지 않습니다.

### 절전 방지 스크립트 로컬 검증

필요한 경우 선택적 테스트 도구와 Chromium을 설치합니다.

```bash
python -m pip install playwright==1.63.0
python -m playwright install chromium
python scripts/keep_alive.py
python -m pytest test/keep_alive_test.py
```

`python scripts/keep_alive.py`는 공개 앱에 접속해 복구를 확인합니다. 테스트는 로컬 재현 화면에서 Chromium을 실행하며 공개 앱에 접속하지 않습니다. Playwright가 설치되지 않았으면 테스트를 건너뜁니다.

## 라이선스

이 저장소의 코드는 MIT 라이선스로 공개합니다. 자세한 내용은 [LICENSE.txt](LICENSE.txt)를 참고하세요.
