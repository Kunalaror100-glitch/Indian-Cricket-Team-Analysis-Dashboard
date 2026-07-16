import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt
import base64 
import random
from pathlib import Path
import time
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Indian Cricket ODI Analysis",page_icon="🏏",layout="wide")

df=pd.read_csv("ODI.csv")
backgrounds = [
    "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?auto=format&fit=crop&w=1920&q=80",  # Cricket stadium
    "https://images.unsplash.com/photo-1531415074968-036ba1b575da?auto=format&fit=crop&w=1920&q=80",  # Cricket ground
    "https://images.unsplash.com/photo-1517927033932-b3d18e61fb3a?auto=format&fit=crop&w=1920&q=80",  # Cricket pitch
    "https://images.unsplash.com/photo-1508098682722-e99c643e7485?auto=format&fit=crop&w=1920&q=80"   # Cricket stadium lights
]

if "background" not in st.session_state:
    st.session_state.background = random.choice(backgrounds)

st.markdown(f"""
<style>
.stApp {{
    background-image:
    linear-gradient(rgba(0,0,0,.75), rgba(0,0,0,.75)),
    url("{st.session_state.background}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.image("https://7cricinr.com/blog/wp-content/uploads/2023/08/AXAR-PATEL-5.png",width=300)

    opt=option_menu(menu_title="Menu",options=["Home","Dataset","Preprocessing","Visualization","About"],icons=["house","table","gear","bar-chart","person"])

if opt == "Home":

    st.markdown("""
<h1 style='text-align:center; color:#FFD700;'>
🏏 Welcome To Indian Cricket Team ODI Analysis Dashboard
</h1>

<h4 style='text-align:center; color:white;'>
Analyze • Visualize • Explore ODI Statistics
</h4>

<hr style="border:1px solid #FFD700;">
""", unsafe_allow_html=True)

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric("🏏Total Matches",df["Match_no"].count())

    with col2:
        st.metric("Total Runs""",df["Runs"].sum())

    with col3:
        st.metric("Total 4's",df["4s"].sum())

    with col4:
        st.metric("Total sixes",df["6s"].sum())
    st.markdown("""<hr style="border:1px solid #FFD700;">""",unsafe_allow_html=True)
    

    st.subheader("🏏 India's Greatest ODI Matches")

    matches = [
    {
        "title": "🏆 ODI Cricket World Cup Final 1983",
        "vs": "India vs West Indies",
        "date": "25 June 1983",
        "result": "India won by 43 runs",
        "highlight": "Kapil Dev lifted India's first-ever ODI World Cup after defending just 183."
    },
    {
        "title": "🔥 ODI Series Final 2002",
        "vs": "India vs England",
        "date": "13 July 2002",
        "result": "India won by 2 wickets",
        "highlight": "Yuvraj Singh and Mohammad Kaif chased 326 at Lord's in one of India's greatest ODI victories."
    },
    {
        "title": "💯 Sachin's Double Century",
        "vs": "India vs South Africa",
        "date": "24 February 2010",
        "result": "India won by 153 runs",
        "highlight": "Sachin Tendulkar became the first cricketer to score an unbeaten 200 in ODI cricket."
    },
    {
        "title": "🏆ODI Cricket World Cup Final 2011",
        "vs": "India vs Sri Lanka",
        "date": "2 April 2011",
        "result": "India won by 6 wickets",
        "highlight": "MS Dhoni's unbeaten 91* guided India to its second ODI World Cup title."
    },
    {
        "title": "🏆 ODI Champions Trophy Final 2013",
        "vs": "India vs England",
        "date": "23 June 2013",
        "result": "India won by 5 runs",
        "highlight": "Ravindra Jadeja and Ishant Sharma helped India win the Champions Trophy in a thrilling final."
    },
    {
        "title": "⚡ Highest Successful ODI Chase vs Australia",
        "vs": "India vs Australia",
        "date": "2 November 2013",
        "result": "India won by 6 wickets",
        "highlight": "Virat Kohli blasted 115 off just 66 balls as India chased 360 in Jaipur."
    },
    {
        "title": "🏆 ODI cup Final 2018",
        "vs": "India vs Bangladesh",
        "date": "28 September 2018",
        "result": "India won by 3 wickets",
        "highlight": "Kedar Jadhav hit the winning runs off the final ball to secure India's seventh Asia Cup title."
    },
    {
        "title": "🏆 ODI Cup Final 2023",
        "vs": "India vs Sri Lanka",
        "date": "17 September 2023",
        "result": "India won by 10 wickets",
        "highlight": "Mohammed Siraj's sensational spell of 6/21 bowled Sri Lanka out for just 50."
    },
    {
        "title": "🏆 ODI Cricket World Cup 2023 Semi-final",
        "vs": "India vs New Zealand",
        "date": "15 November 2023",
        "result": "India won by 70 runs",
        "highlight": "Virat Kohli scored his record-breaking 50th ODI century and Mohammed Shami took 7 wickets."
    }
]

    cols = st.columns(3)

    for i, match in enumerate(matches):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="
                background:#1b263b;
                padding:18px;
                border-radius:12px;
                border:2px solid #FFD700;
                margin-bottom:18px;
                color:white;
                box-shadow:0 0 10px rgba(255,215,0,0.3);
            ">
                <h4 style="color:#FFD700;">{match['title']}</h4>
                <p><b>{match['vs']}</b></p>
                <p>📅 {match['date']}</p>
                <p>🏏 {match['result']}</p>
                <hr>
                <p style="font-size:14px;">{match['highlight']}</p>
            </div>
            """, unsafe_allow_html=True)

elif opt=="Dataset":
    st.title("📂 Dataset Overview")

    col1,col2,col3=st.columns(3)

    col1.metric("Rows",df.shape[0])
    col3.metric("Columns",df.shape[1])

    st.write("---")

    tab1,tab2,tab3=st.tabs(["Dataset","Data Types","Statistics"])

    with tab1:
        Slider=st.slider("data",10,500)
        st.write(df.head(Slider))

    with tab2:
        dtype=pd.DataFrame({"Column":df.columns,"Datatype":df.dtypes.astype(str)})
        st.write(dtype)

    with tab3:
        st.dataframe(df.describe())

elif opt=="Preprocessing":


    st.title("🧹 Data Preprocessing")

    tab1,tab2=st.tabs(["Missing Values","Duplicates"])
    with tab1:

        st.subheader("Null Values")

        missing=df.isnull().sum()

        st.dataframe(pd.DataFrame({"Column":missing.index,"Null Values":missing.values}))

    with tab2:

        st.subheader("Duplicate Records")

        duplicate=df.duplicated().sum()

        st.metric("duplicate values",duplicate)

elif opt=="Visualization":

    st.title("📊 Batting Performance Dashboard")

    player = st.selectbox("Select Player",["All"] + sorted(df["Batsman_Name"].unique()))

    data = df.copy()

    if player != "All":
        data = data[data["Batsman_Name"] == player]

    tab1,tab2, tab3, tab4 = st.tabs(["Top Player's","Player's Performance","Dismissal Analysis","Player's Comparison"])

    with tab1:

        c1, c2 = st.columns(2)

        with c1:

            top_runs = (df.groupby("Batsman_Name", as_index=False)["Runs"].sum().nlargest(20, "Runs"))
            fig = px.bar(
                top_runs,
                x="Batsman_Name",
                y="Runs",
                color="Runs",
                text="Runs",
                title="Top 20 Run Scorers"
            )

            st.plotly_chart(fig, use_container_width=True)

        with c2:

            top_sr = (
                data.groupby("Batsman_Name")["Strike_Rate"]
                .mean()
                .sort_values(ascending=False)
                .head(20)
                .reset_index()
            )

            fig = px.bar(
                top_sr,
                x="Batsman_Name",
                y="Strike_Rate",
                color="Strike_Rate",
                title="Strike Rate"
            )

            st.plotly_chart(fig, use_container_width=True)

        c3, c4 = st.columns(2)

        with c3:

            top4 = (
                data.groupby("Batsman_Name")["4s"]
                .sum()
                .sort_values(ascending=False)
                .head(20)
                .reset_index()
            )

            fig = px.bar(
                top4,
                x="Batsman_Name",
                y="4s",
                color="4s",
                title="Fours"
            )

            st.plotly_chart(fig, use_container_width=True)

        with c4:

            top6 = (
                data.groupby("Batsman_Name")["6s"]
                .sum()
                .sort_values(ascending=False)
                .head(20)
                .reset_index()
            )

            fig = px.bar(
                top6,
                x="Batsman_Name",
                y="6s",
                color="6s",
                title="Sixes"
            )

            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        Slider=st.slider("Select No. of data",20,490)

        c1, c2 = st.columns(2)

        with c1:

            fig = px.scatter(
                data.head(Slider),
                x="Balls",
                y="Runs",
                color="Strike_Rate",
                hover_name="Batsman_Name",
                size="Runs",
                title="Runs vs Balls"
            )

            st.plotly_chart(fig, use_container_width=True)

        with c2:

            fig = px.scatter(
                data.head(Slider),
                x="Runs",
                y="Strike_Rate",
                color="Runs",
                size="Match_no",
                hover_name="Batsman_Name",
                title="performance by matches"
            )

            st.plotly_chart(fig, use_container_width=True)
        
        performance = (
    data.groupby("Batsman_Name")
    .agg(
        Runs=("Runs", "sum"),
        Matches=("Match_no", "nunique")
    )
    .reset_index()
)


        performance["Average_Runs"] = (
        performance["Runs"] / performance["Matches"].head(Slider)).round(2)

        fig = px.bar(
            performance.sort_values("Average_Runs", ascending=False).head(10),
            x="Batsman_Name",
            y="Average_Runs",
            color="Average_Runs",
            title="Top Players by Average Runs"
        )

        st.plotly_chart(fig, use_container_width=True)


    # with tab3:

    #     c1, c2 = st.columns(2)

    #     with c1:

    #         fig = px.histogram(
    #             data,
    #             x="Runs",
    #             nbins=25,
    #             title="Runs Distribution"
    #         )

    #         st.plotly_chart(fig, use_container_width=True)

    #     with c2:

    #         fig = px.histogram(
    #             data,
    #             x="Strike_Rate",
    #             nbins=25,
    #             title="Strike Rate Distribution"
    #         )

    #         st.plotly_chart(fig, use_container_width=True)

    #     c3, c4 = st.columns(2)

    #     with c3:

    #         fig = px.box(
    #             data,
    #             y="Runs",
    #             title="Runs Box Plot"
    #         )

    #         st.plotly_chart(fig, use_container_width=True)

    #     with c4:

    #         fig = px.violin(
    #             data,
    #             y="Runs",
    #             box=True,
    #             title="Runs Violin Plot"
    #         )

    #         st.plotly_chart(fig, use_container_width=True)

        with tab3:

            dismissal = (
                data["Dismissal"]
                .value_counts()
                .reset_index()
            )

            dismissal.columns = [
                "Dismissal",
                "Count"
            ]

            fig = px.pie(
                dismissal,
                names="Dismissal",
                values="Count",
                hole=0.45,
                title="Dismissal Type Percentage"
            )

            st.plotly_chart(fig, use_container_width=True)

            player_stats = (
                data.groupby("Batsman_Name")
                .agg(
                    Total_Runs=("Runs", "sum"),
                    Matches_Played=("Match_no", "nunique")
                )
                .reset_index()
            )

            fig = px.treemap(
                player_stats,
                path=["Batsman_Name"],
                values="Total_Runs",
                hover_data=["Matches_Played"],
                title="Player Runs Treemap"
            )

            fig.update_traces(
                textinfo="label+value",
                hovertemplate="<b>%{label}</b><br>"
                            "🏃 Total Runs: %{value}<br>"
                            "🏏 Matches Played: %{customdata[0]}<extra></extra>"
            )

            st.plotly_chart(fig, use_container_width=True)

            sunburst_data = (
                data.groupby(["Batsman_Name", "Dismissal"])
                .size()
                .reset_index(name="Count")
            )

            fig = px.sunburst(
                sunburst_data,
                path=["Batsman_Name", "Dismissal"],
                values="Count",
                title="Dismissal Percentage by Player"
            )

            fig.update_traces(
                textinfo="label+percent parent",
                hovertemplate="<b>%{label}</b><br>"
                            "Percentage: %{percentParent:.1%}<extra></extra>"
            )

            st.plotly_chart(fig, use_container_width=True)

    with tab4:

        st.subheader("👤 Player Comparison Dashboard")

        players = sorted(df["Batsman_Name"].unique())

        col1, col2 = st.columns(2)

        with col1:
            player1 = st.selectbox("Select Player 1", players)

        with col2:
            player2 = st.selectbox(
                "Select Player 2",
                players,
                index=1 if len(players) > 1 else 0
            )

        p1 = df[df["Batsman_Name"] == player1]
        p2 = df[df["Batsman_Name"] == player2]

        summary = pd.DataFrame({

            "Statistic":[
                "Matches",
                "Runs",
                "Highest Score",
                "Average Strike Rate",
                "Fours",
                "Sixes"
            ],

            player1:[

                len(p1),
                p1["Runs"].sum(),
                p1["Runs"].max(),
                round(p1["Strike_Rate"].mean(),2),
                p1["4s"].sum(),
                p1["6s"].sum()
            ],

            player2:[

                len(p2),
                p2["Runs"].sum(),
                p2["Runs"].max(),
                round(p2["Strike_Rate"].mean(),2),
                p2["4s"].sum(),
                p2["6s"].sum()
            ]

        })

        st.dataframe(summary, use_container_width=True)

        st.divider()

        fig = px.bar(

            summary,

            x="Statistic",

            y=[player1, player2],

            barmode="group",

            title="Player Comparison"

        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        st.subheader("Runs Progress")

        compare = pd.concat([

            p1.assign(Player=player1),

            p2.assign(Player=player2)

        ])

        fig = px.line(

            compare,

            x="Match_no",

            y="Runs",

            color="Player",

            markers=True,

            title="Runs in Each Match"

        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        st.subheader("Batting Position Analysis")

        batting = (

            compare.groupby(

                ["Player","Batting_Position"]

            )["Runs"]

            .sum()

            .reset_index()

        )

        fig = px.bar(

            batting,

            x="Batting_Position",

            y="Runs",

            color="Player",

            barmode="group",

            title="Runs by Batting Position"

        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        st.subheader("Dismissal Comparison")

        dismissal = (

            compare.groupby(

                ["Player","Dismissal"]

            )

            .size()

            .reset_index(name="Count")

        )

        fig = px.bar(

            dismissal,

            x="Dismissal",

            y="Count",

            color="Player",

            barmode="group",

            title="Dismissal Types"

        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        st.subheader("Boundary Comparison")

        boundary = pd.DataFrame({

            "Boundary":["4s","6s"],

            player1:[
                p1["4s"].sum(),
                p1["6s"].sum()
            ],

            player2:[
                p2["4s"].sum(),
                p2["6s"].sum()
            ]

        })

        fig = px.bar(

            boundary,

            x="Boundary",

            y=[player1,player2],

            barmode="group",

            title="Boundary Comparison"

        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        st.subheader("Bubble Chart")

        fig = px.scatter(

            compare,

            x="Balls",

            y="Runs",

            color="Player",

            size="Strike_Rate",

            hover_name="Batsman_Name",

            title="Runs vs Balls"

        )

        st.plotly_chart(fig, use_container_width=True)
        st.divider()

        year = (
    compare.groupby(["Year","Player"])["Runs"]
    .mean()
    .reset_index()
)

        fig = px.line(
            year,
            x="Year",
            y="Runs",
            color="Player",
            markers=True,
            title="Average Runs by Year"
        )

        st.plotly_chart(fig, use_container_width=True)
        st.divider()
        fig = px.strip(compare,
    x="Player",
    y="Runs",
    color="Player",
    title="Runs in Every Match")
        fig = px.strip(
    compare,
    x="Player",
    y="Runs",
    color="Player",
    hover_data=["Match_no"],
    title="Runs in Every Match"
)

        st.plotly_chart(fig, use_container_width=True)
        
elif opt=="About":
    st.markdown("""
<h1 style='text-align:center;color:#FFD700;'>
🏏 About the Project
</h1>

<p style='text-align:center;font-size:18px;color:white;'>
Indian Cricket Team ODI Analysis Dashboard
</p>
""", unsafe_allow_html=True)
    st.markdown("""
<div style="
background:rgba(255,255,255,0.08);
padding:20px;
border-radius:15px;
border-left:6px solid #FFD700;
margin-bottom:20px;">

<h3 style="color:#FFD700;">📖 Project Overview</h3>

<p style="font-size:17px; line-height:1.8; color:white;">
This project is developed using <b>Python</b>, <b>Streamlit</b>,
<b>Pandas</b>, <b>NumPy</b>, <b>Plotly</b>,
<b>Matplotlib</b>, and <b>Seaborn</b>.
It provides an interactive platform to analyze the batting
performance of the <b>Indian Cricket Team</b> in One Day Internationals (ODIs).
The dashboard transforms raw cricket statistics into meaningful
visualizations, making it easier to explore player performance,
team trends, and match insights.
</p>

</div>
""", unsafe_allow_html=True)
    left, right = st.columns(2)
    with left:

     st.markdown("""
    <div style="
    background:rgba(255,255,255,0.08);
    padding:18px;
    border-radius:12px;
    margin-bottom:20px;">

    <h3 style="color:#FFD700;">🎯 Objectives</h3>

    ✔ Analyze batting performance of Indian players.<br>
    ✔ Compare runs, strike rate, boundaries and averages.<br>
    ✔ Identify top performers across matches and years.<br>
    ✔ Discover performance trends using charts.<br>
    ✔ Help fans and analysts understand ODI statistics.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="
background:rgba(255,255,255,0.08);
padding:18px;
border-radius:12px;
color:white;">

<h3 style="color:#FFD700;">⚙ Technologies Used</h3>

🐍 Python<br>
🚀 Streamlit<br>
🐼 Pandas<br>
🔢 NumPy<br>
📊 Plotly Express<br>
📈 Matplotlib<br>
🎨 Seaborn

</div>
""", unsafe_allow_html=True)
    with right:

     st.markdown("""
    <div style="
    background:rgba(255,255,255,0.08);
    padding:18px;
    border-radius:12px;
    margin-bottom:20px;">

    <h3 style="color:#FFD700;">✨ Features</h3>

    🏏 Player-wise Analysis<br>
    📅 Match-wise Analysis<br>
    📆 Year-wise Analysis<br>
    🏆 Top Run Scorers<br>
    📊 Interactive Charts<br>
    🎛 Dynamic Filters<br>
    📈 Batting Comparison

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
    background:rgba(255,255,255,0.08);
    padding:18px;
    border-radius:12px;">"""

     ,unsafe_allow_html=True)
    st.markdown("""
<div style="
background:rgba(255,255,255,0.08);
padding:20px;
border-radius:15px;
border-left:6px solid #FFD700;
margin-top:20px;">

<h3 style="color:#FFD700;">🌟 Benefits</h3>

✅ Explore player performances interactively.<br>
✅ Compare batting statistics across matches and years.<br>
✅ Identify trends and consistency of players.<br>
✅ Gain data-driven insights into ODI cricket.<br>
✅ Learn practical data analytics and visualization techniques.

</div>
""", unsafe_allow_html=True)
    st.header("✨ Dashboard Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("👤 Player Analysis")
        st.success("🏏 Batting Analysis")
        st.success("🎯 Bowling Analysis")
        st.success("📊 Match Analysis")

    with col2:
        st.success("🏆 Team Records")
        st.success("📈 Interactive Charts")
        st.success("⚖️ Player Comparison")
        st.success("📅 Year-wise Analysis")
    st.markdown("""
<div style="
    background: rgba(255,255,255,0.08);
    border-left: 6px solid #FFD700;
    padding: 20px;
    border-radius: 12px;
    color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
">

<h2 style="color:#FFD700; margin-bottom:10px;">
🏏 Project Summary
</h2>

<p style="font-size:17px; line-height:1.8;">
📊 This dashboard demonstrates how <b>Data Analytics</b> can be applied to
<b>Indian Cricket Team ODI</b> performance using <b>Python</b>,
<b>Pandas</b>, <b>Plotly</b>, and <b>Streamlit</b>.
</p>

<p style="font-size:17px; line-height:1.8;">
📈 Interactive visualizations help analyze batting, bowling, team performance,
match results, and player statistics in an easy-to-understand way.
</p>

<p style="font-size:17px; line-height:1.8;">
🎯 The objective is to transform complex cricket data into meaningful insights,
making performance analysis simple, engaging, and accessible for cricket fans,
students, and data enthusiasts.
</p>

</div>
""", unsafe_allow_html=True)