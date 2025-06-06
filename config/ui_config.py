# config/ui_config.py
class UIConfig:
    SCREEN_SIZE = (1080, 740)

    # 색상
    BG_COLOR = (216, 107, 107)
    TEXT_COLOR = (255, 255, 255)
    BUTTON_COLOR = (255, 255, 255)
    BUTTON_TEXT_COLOR = (216, 107, 107)
    INPUT_ACTIVE_COLOR = (200, 200, 200)
    INPUT_INACTIVE_COLOR = (255, 255, 255)
    BLACK_COLOR = (0, 0, 0)

    # 폰트 크기
    TITLE_FONT_SIZE = 32
    BUTTON_FONT_SIZE = 24

    # 버튼 크기와 간격
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 80
    BUTTON_SPACING = 100
    BUTTON_START_X = 440
    BUTTON_START_Y = 250

    # 입력 필드 설정
    INPUT_FIELD_WIDTH = 400
    INPUT_FIELD_HEIGHT = 50
    INPUT_FIELD_START_X = 340
    INPUT_FIELD_START_Y = 200
    INPUT_FIELD_SPACING = 100

    # 레이블 위치
    LABEL_X = 200
    LABEL_Y_START = 215
    LABEL_Y_SPACING = 100
    LABEL_X_DICE = 550
    LABEL_Y_DICE = 500

    # UI 요소 위치
    TITLE_POS = (460, 100)
    SUBTITLE_POS = (400, 180)

    # 버튼 위치와 크기
    BACK_BUTTON_RECT = (50, 50, 100, 50)
    START_BUTTON_RECT = (440, 650, 200, 50)
    DICE_BUTTON_RECT = (500, 550, 150, 50)
