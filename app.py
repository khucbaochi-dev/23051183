"""
app.py — AIDEOM-VN | Trang chủ
================================
Mô hình ra quyết định phát triển kinh tế Việt Nam trong kỉ nguyên AI.
12 bài tập theo 4 cấp độ (Dễ / Trung bình / Khá khó / Khó).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st
from src.data_loader import load_macro
from src.utils import page_header

st.set_page_config(
    page_title="AIDEOM-VN — Mô hình ra quyết định KT Việt Nam",
    page_icon="🇻🇳",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────────────────────────
st.markdown("# 🇻🇳 AIDEOM-VN")
st.markdown("#### *AI-Driven Decision Optimization Model for Vietnam*")
st.markdown(
    "Web app giải **12 bài toán mô hình ra quyết định** phát triển kinh tế "
    "Việt Nam trong kỉ nguyên AI — dữ liệu thực 2020-2025."
)

st.divider()

# ─────────────────────────────────────────────────────────────────
# KPI ngang (lấy từ data thực, năm gần nhất)
# ─────────────────────────────────────────────────────────────────
macro = load_macro()
latest = macro.iloc[-1]
prev = macro.iloc[-2]

c1, c2, c3, c4 = st.columns(4)
c1.metric(
    "GDP 2025",
    f"{latest['GDP_billion_USD']:,.1f} tỷ USD",
    f"+{latest['GDP_growth_pct']:.2f}%",
)
c2.metric(
    "Kinh tế số / GDP",
    f"≈{latest['digital_economy_share_GDP_pct']:.1f}%",
    f"+{latest['digital_economy_share_GDP_pct'] - prev['digital_economy_share_GDP_pct']:.1f} đpt",
)
c3.metric(
    "FDI giải ngân 2025",
    f"{latest['FDI_disbursed_billion_USD']:.1f} tỷ USD",
    f"+{(latest['FDI_disbursed_billion_USD'] / prev['FDI_disbursed_billion_USD'] - 1) * 100:.1f}%",
)
c4.metric(
    "GDP/người 2025",
    f"{latest['GDP_per_capita_USD']:,.0f} USD",
    f"+{(latest['GDP_per_capita_USD'] / prev['GDP_per_capita_USD'] - 1) * 100:.1f}%",
)

st.divider()

# ─────────────────────────────────────────────────────────────────
# 12 bài toán theo 4 cấp độ
# ─────────────────────────────────────────────────────────────────
st.markdown("## 📚 12 bài toán theo 4 cấp độ")

LEVELS = [
    {
        "icon": "🟢",
        "name": "Cấp độ DỄ — Làm quen mô hình",
        "items": [
            ("Bài 1", "Hàm sản xuất Cobb-Douglas mở rộng + AI — Growth accounting, dự báo GDP 2030", "pages/01_Bai1_Cobb_Douglas.py"),
            ("Bài 2", "LP phân bổ ngân sách 4 hạng mục — scipy.optimize, shadow price", "pages/02_Bai2_LP_NganSach.py"),
            ("Bài 3", "Chỉ số ưu tiên 10 ngành — Min-max norm, weighted scoring, sensitivity", "pages/03_Bai3_Priority_NganhT.py"),
        ],
    },
    {
        "icon": "🟡",
        "name": "Cấp độ TRUNG BÌNH — Tối ưu cổ điển",
        "items": [
            ("Bài 4", "LP phân bổ ngân sách số theo ngành - vùng — PuLP & CVXPY, 24 biến", "pages/04_Bai4_LP_Nganh_Vung.py"),
            ("Bài 5", "MIP lựa chọn 15 dự án chuyển đổi số — Knapsack tổng quát hóa", "pages/05_Bai5_MIP_15_DuAn.py"),
            ("Bài 6", "TOPSIS xếp hạng 6 vùng đầu tư AI — Entropy weight", "pages/06_Bai6_TOPSIS_6Vung.py"),
        ],
    },
    {
        "icon": "🟠",
        "name": "Cấp độ KHÁ KHÓ — Đa mục tiêu & động",
        "items": [
            ("Bài 7", "Tối ưu đa mục tiêu Pareto NSGA-II — pymoo, 4 mục tiêu", "pages/07_Bai7_NSGA2_Pareto.py"),
            ("Bài 8", "Tối ưu động liên thời gian 2026-2035 — Ramsey, CVXPY", "pages/08_Bai8_Dong_2026_2035.py"),
            ("Bài 9", "Tác động AI tới lao động Việt Nam — NetJob 8 ngành", "pages/09_Bai9_LaoDong_AI.py"),
        ],
    },
    {
        "icon": "🔴",
        "name": "Cấp độ KHÓ — Ngẫu nhiên & học tăng cường",
        "items": [
            ("Bài 10", "Quy hoạch ngẫu nhiên 2 giai đoạn — Pyomo, VSS/EVPI", "pages/10_Bai10_Stochastic_SP.py"),
            ("Bài 11", "Q-learning cho chính sách kinh tế thích nghi — MDP 81 trạng thái", "pages/11_Bai11_QLearning_RL.py"),
            ("Bài 12", "AIDEOM tích hợp — Dashboard 6 module, 5 kịch bản", "pages/12_Bai12_AIDEOM_TichHop.py"),
        ],
    },
]

for level in LEVELS:
    with st.expander(f"{level['icon']} {level['name']}", expanded=(level['icon'] == "🟢")):
        for code, desc, path in level["items"]:
            cols = st.columns([1, 6, 2])
            cols[0].markdown(f"**{code}**")
            cols[1].markdown(desc)
            cols[2].page_link(path, label="Mở bài →")

st.divider()

# ─────────────────────────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🇻🇳 AIDEOM-VN")
    st.caption("Mô hình ra quyết định phát triển kinh tế VN trong kỉ nguyên AI")
    st.divider()
    st.caption("📊 Dữ liệu: NSO, MoST, MIC, MPI, WB, GII 2025")
    st.caption("📋 Theo bộ bài tập 'Các mô hình ra quyết định'")
