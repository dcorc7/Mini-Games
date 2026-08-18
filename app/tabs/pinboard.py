import streamlit as st
import base64
from pathlib import Path
from io import BytesIO
from PIL import Image
import textwrap

APP_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = APP_DIR / "assets"

MAX_DIMENSION = 500


@st.cache_data
def _img_to_base64(path_str: str) -> str:
    path = Path(path_str)
    img = Image.open(path)
    img.thumbnail((MAX_DIMENSION, MAX_DIMENSION))
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=85)
    encoded = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/jpeg;base64,{encoded}"


def render_pinboard(photo_paths: list[str], event_details: dict):
    layout = [
        (5, 3, -7, 140),
        (5, 20, -8, 140),
        (5, 68, 5, 130),
        (5, 85, 4, 130),
        (40, 3, 4, 120),
        (40, 20, -7, 120),
        (40, 68, 5, 140),
        (40, 85, -6, 140),
        (70, 3, -5, 130),
        (70, 20, 6, 120),
        (70, 68, -7, 130),
        (70, 85, 5, 130),
    ]

    photos_html = ""
    for i, filename in enumerate(photo_paths[:len(layout)]):
        top, left, rot, size = layout[i]
        full_path = ASSETS_DIR / filename

        if not full_path.exists():
            st.warning(f"Image not found: {full_path}")
            continue

        try:
            data_uri = _img_to_base64(str(full_path))
        except Exception as e:
            st.warning(f"Could not load {filename}: {e}")
            continue

        # Note: no leading indentation on these lines
        photos_html += (
            f'<div style="position:absolute; top:{top}%; left:{left}%; '
            f'transform: rotate({rot}deg); background:white; padding:10px 10px 25px 10px; '
            f'box-shadow: 3px 3px 12px rgba(0,0,0,0.35); border-radius:2px; z-index:1;">'
            f'<div style="position:absolute; top:-14px; left:50%; transform:translateX(-50%); '
            f'font-size:24px; filter: drop-shadow(1px 2px 2px rgba(0,0,0,0.4));">📌</div>'
            f'<img src="{data_uri}" style="width:{size}px; height:{size}px; object-fit:cover; display:block;"{i}>'
            f'</div>'
        )

    invite_html = (
        '<div style="position:absolute; top:50%; left:50%; '
        'transform: translate(-50%, -50%) rotate(-1deg); background: #fffaf0; '
        'border: 2px solid #d8c9a3; border-radius:6px; padding:35px 45px; width:340px; '
        'text-align:center; box-shadow: 0 8px 24px rgba(0,0,0,0.45); z-index:10;">'
        '<div style="position:absolute; top:-16px; left:50%; transform:translateX(-50%); font-size:26px;">📌</div>'
        f'<p style="font-family:\'Georgia\', serif; font-size:14px; letter-spacing:3px; color:#9a3324; margin:0;">'
        f'{event_details.get("title", "You\'re Invited")}</p>'
        f'<h2 style="font-family:\'Georgia\', serif; color:#333; margin:10px 0;">'
        f'{event_details.get("names", "")}</h2>'
        f'<p style="font-family:\'Georgia\', serif; color:#555; font-size:16px; margin:4px 0;">'
        f'{event_details.get("date", "")}</p>'
        f'<p style="font-family:\'Georgia\', serif; color:#555; font-size:16px; margin:4px 0;">'
        f'{event_details.get("time", "")}</p>'
        f'<p style="font-family:\'Georgia\', serif; color:#9a3324; font-size:16px; margin-top:10px; font-weight:bold;">'
        f'{event_details.get("location", "")}</p>'
        '</div>'
    )

    board_html = (
        '<div style="position:relative; width:100%; height:700px; '
        'background: repeating-linear-gradient(45deg, #c9a26d, #c9a26d 2px, #b8925c 2px, #b8925c 4px); '
        'border-radius:12px; box-shadow: inset 0 0 60px rgba(0,0,0,0.3); overflow:hidden;">'
        f'{photos_html}{invite_html}'
        '</div>'
    )

    st.markdown(board_html, unsafe_allow_html=True)