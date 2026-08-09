import streamlit as st
import streamlit.components.v1 as components

# ---------------------
# ----- HOME PAGE -----
# ---------------------

def render_schedule():
    st.write("")

    page_cols = st.columns([1, 1])

    with page_cols[0]:
        st.markdown("""<h3 style=\"text-align: center; 
                            font-family: Georgia, 'Times New Roman', serif;
                            font-weight: 400;
                            letter-spacing: 0.14em;
                            text-transform: uppercase;
                            font-size: 26px;
                            margin: 0 0 18px;
                            border-bottom: 1px solid\">
                    Schedule
            </h3>""", unsafe_allow_html=True)

        # Define your fixed daily schedule items
        schedule = [
            {
                "time": "08:00 AM", 
                "task": "FILL IN"
            },
            {
                "time": "09:30 AM", 
                "task": "FILL IN"
            },
            {
                "time": "11:00 AM", 
                "task": "FILL IN"
            },
            {
                "time": "01:00 PM", 
                "task": "FILL IN"
            },
            {
                "time": "02:00 PM", 
                "task": "FILL IN"
            },
            {
                "time": "04:30 PM", 
                "task": "FILL IN"
             },
        ]

        # Rendering the vertical timeline using columns
        for item in schedule:
            schedule_col1, schedule_col2 = st.columns([1, 4])

            with schedule_col1:
                st.markdown(
                    f"<span style='color: #9a3324; font-weight: 700;'>{item['time']}</span>",
                    unsafe_allow_html=True
                )
            with schedule_col2:
                st.markdown(
                    f"<div style='background-color: #f6f1e7; color: #1b1815; padding: 10px 14px; "
                    f"border-radius: 6px; border-left: 4px solid #9a3324;'>{item['task']}</div>",
                    unsafe_allow_html=True
                )

            # small gap
            st.write("")

    with page_cols[1]:
        st.markdown("""<h3 style=\"text-align: center; 
                                    font-family: Georgia, 'Times New Roman', serif;
                                    font-weight: 400;
                                    letter-spacing: 0.14em;
                                    text-transform: uppercase;
                                    font-size: 26px;
                                    margin: 0 0 10px;
                                    border-bottom: 1px solid\">
                            UCHI Menu
                    </h3>""", unsafe_allow_html=True)

        uchi_menu_html = ("""
            <section class="uchi-menu">
            <style>
                .uchi-menu {
                    --ink: #1b1815;
                    --paper: #f6f1e7;
                    --line: #d8cdb8;
                    --accent: #9a3324;
                    --muted: #7a7266;
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                    color: var(--ink);
                    background: var(--paper);
                    max-width: 1100px;
                    margin: 0 auto;
                    padding: 56px 32px 80px;
                    box-sizing: border-box;
                    border-radius: 6px;
                }

                .uchi-menu *{box-sizing:border-box;}

                .uchi-menu .menu-grid{
                    display:grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 0 48px;
                }

                .uchi-menu .menu-section{
                    break-inside: avoid;
                    margin-bottom: 40px;
                }

                .uchi-menu .menu-section h2{
                    font-family: Georgia, 'Times New Roman', serif;
                    font-weight: 400;
                    font-style: italic;
                    font-size: 20px;
                    letter-spacing: 0.03em;
                    margin: 0 0 16px;
                    padding-bottom: 8px;
                    border-bottom: 1px solid var(--accent);
                    display:inline-block;
                }

                .uchi-menu .menu-item{
                    margin-bottom: 14px;
                }

                .uchi-menu .item-row{
                    display:flex;
                    justify-content:space-between;
                    align-items:baseline;
                    gap: 10px;
                }

                .uchi-menu .item-name{
                    font-weight: 600;
                    font-size: 14.5px;
                    letter-spacing: 0.01em;
                }

                .uchi-menu .item-name .raw{
                    color: var(--accent);
                    font-weight: 700;
                }

                .uchi-menu .item-price{
                    font-size: 13.5px;
                    color: var(--accent);
                    white-space: nowrap;
                    font-variant-numeric: tabular-nums;
                }

                .uchi-menu .item-desc{
                    font-size: 12.5px;
                    color: var(--muted);
                    line-height: 1.4;
                    margin-top: 2px;
                }

                .uchi-menu .menu-footnote{
                    text-align:center;
                    margin-top: 24px;
                    padding-top: 20px;
                    border-top: 1px solid var(--line);
                    font-size: 11.5px;
                    color: var(--muted);
                }

                @media (max-width: 900px){
                    .uchi-menu .menu-grid{ grid-template-columns: repeat(2, 1fr); }
                }

                @media (max-width: 620px){
                    .uchi-menu .menu-grid{ grid-template-columns: 1fr; }
                    .uchi-menu{ padding: 40px 20px 60px; }
                }

            </style>

            <div class="menu-grid">

                <div class="menu-section">
                    <h2>Cool Tastings</h2>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> hirame usuzukuri</span><span class="item-price">23</span></div><div class="item-desc">thinly sliced flounder, candied quinoa, olive oil</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">kinoko usuzukuri</span><span class="item-price">19.5</span></div><div class="item-desc">seasonal mushroom, shallot, shiro zu</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> hama chili</span><span class="item-price">24</span></div><div class="item-desc">yellowtail, ponzu, thai chili, orange suprème</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> wagyu tartare</span><span class="item-price">24</span></div><div class="item-desc">fried jalapeno, cured egg yolk, nuoc mam, chili oil</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> sake tom kha</span><span class="item-price">23</span></div><div class="item-desc">salmon, coconut, lime leaf, dill</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> hotate crudo</span><span class="item-price">23</span></div><div class="item-desc">scallop, passionfruit, apple, aji amarillo</div></div>
                </div>

                <div class="menu-section">
                    <h2>Hot Tastings</h2>
                    <div class="menu-item"><div class="item-row"><span class="item-name">chawanmushi</span><span class="item-price">28</span></div><div class="item-desc">crab, brown butter, bacon</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">walu walu</span><span class="item-price">22</span></div><div class="item-desc">oak-grilled escolar, ponzu, candied citrus, myoga</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> hot rock</span><span class="item-price">23</span></div><div class="item-desc">australian wagyu, kosho tamari butter, whisky maple ponzu</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> kinoko nabe</span><span class="item-price">24.5</span></div><div class="item-desc">seasonal mushroom, tentsuyu, koshihikari rice, egg yolk — with gyutoro +8</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">sasami yaki</span><span class="item-price">18</span></div><div class="item-desc">chicken, coconut milk, cilantro</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">pork belly</span><span class="item-price">26</span></div><div class="item-desc">black bean, coconut, lychee</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">cabbage</span><span class="item-price">18</span></div><div class="item-desc">tofu, pepita furikake</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">denver steak</span><span class="item-price">35</span></div><div class="item-desc">black garlic hoisin, thai basil</div></div>
                </div>

                <div class="menu-section">
                    <h2>Caviar Selection</h2>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> trout roe</span><span class="item-price">35</span></div><div class="item-desc">mild, oceanic salinity, subtle sweet and nutty undertones</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> kaluga</span><span class="item-price">95</span></div><div class="item-desc">medium size pearls, earthy, umami, robust — yuzu crème fraîche, taiyaki, chives</div></div>
                </div>

                <div class="menu-section">
                    <h2>Nigiri / Sashimi</h2>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> madai <em>— japanese sea bream</em></span><span class="item-price">8</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> hamachi <em>— yellowtail</em></span><span class="item-price">8 / 25</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> hirame <em>— flounder</em></span><span class="item-price">6.5 / 21</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> maguro <em>— bigeye tuna loin</em></span><span class="item-price">9 / 32</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> shime saba <em>— norwegian mackerel</em></span><span class="item-price">6.5 / 21</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> boquerones <em>— cured spanish anchovy</em></span><span class="item-price">6.5 / 21</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> sake <em>— atlantic salmon</em></span><span class="item-price">7 / 22</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> sake toro <em>— salmon belly</em></span><span class="item-price">7.5 / 23</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> namahotate <em>— dayboat scallop</em></span><span class="item-price">7.5</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> ikura <em>— salmon roe</em></span><span class="item-price">8</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">avocado <em>— yuzu kosho</em></span><span class="item-price">5</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">kinoko <em>— mushroom</em></span><span class="item-price">7</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">nasu <em>— japanese eggplant</em></span><span class="item-price">5</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">watarigani <em>— blue crab</em></span><span class="item-price">15</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">unagi <em>— freshwater eel</em></span><span class="item-price">7.5</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">gyutoro <em>— 72-hour westholme wagyu</em></span><span class="item-price">16</span></div></div>
                </div>

                <div class="menu-section">
                    <h2>Bluefin Selection</h2>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> bluefin akami <em>— lean tuna</em></span><span class="item-price">15.5 / 40</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> bluefin chutoro <em>— medium fatty tuna</em></span><span class="item-price">16.5 / 50</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> bluefin otoro <em>— extra fatty tuna</em></span><span class="item-price">18.5 / 65</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> bluefin otoro gunkan <em>— fatty tuna tartare</em></span><span class="item-price">15</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> bluefin akami zuke <em>— marinated lean tuna</em></span><span class="item-price">15.5 / 40</span></div></div>
                </div>

                <div class="menu-section">
                    <h2>Toyosu</h2>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> suzuki <em>— japanese sea perch</em></span><span class="item-price">8</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> kurodai <em>— baby black snapper</em></span><span class="item-price">11</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> kinmedai <em>— goldeneye snapper</em></span><span class="item-price">12 / 44</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> shima aji <em>— striped jack</em></span><span class="item-price">11 / 40</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> engawa <em>— fluke wing</em></span><span class="item-price">9</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> kanpachi <em>— amberjack</em></span><span class="item-price">9 / 36</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> masu <em>— tasmanian ocean trout</em></span><span class="item-price">8 / 24</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> dry aged ora king <em>— dry aged big glory bay salmon</em></span><span class="item-price">13 / 43</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> dry aged hamachi <em>— dry aged yellowtail</em></span><span class="item-price">12 / 44</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> dry aged sawara <em>— dry aged spanish mackerel</em></span><span class="item-price">11 / 42</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> masaba <em>— japanese mackerel</em></span><span class="item-price">11</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> muki hotate <em>— hokkaido scallop</em></span><span class="item-price">12</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> hokkaido uni <em>— premium japanese sea urchin</em></span><span class="item-price">20</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> trout roe gunkan <em>— trout roe</em></span><span class="item-price">10</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> caviar gunkan <em>— kaluga hybrid</em></span><span class="item-price">25</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">a5 <em>— wagyu beef</em></span><span class="item-price">22</span></div></div>
                </div>

                <div class="menu-section">
                    <h2>Yasaimono</h2>
                    <div class="menu-item"><div class="item-row"><span class="item-name">edamame</span><span class="item-price">11</span></div><div class="item-desc">grilled soybeans</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">uchi salad</span><span class="item-price">15.5</span></div><div class="item-desc">baby greens, daikon, edamame, jalapeño puree</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">seaweed salad</span><span class="item-price">12</span></div><div class="item-desc">cucumber, green apple, sesame</div></div>
                </div>

                <div class="menu-section">
                    <h2>Agemono</h2>
                    <div class="menu-item"><div class="item-row"><span class="item-name">ebi</span><span class="item-price">11</span></div><div class="item-desc">shrimp tempura</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">kabocha</span><span class="item-price">11</span></div><div class="item-desc">japanese pumpkin tempura</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">hana</span><span class="item-price">10</span></div><div class="item-desc">cauliflower tempura</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">market vegetable</span><span class="item-price">15</span></div><div class="item-desc">szechuan black vinegar, chili crisp</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">karaage</span><span class="item-price">17</span></div><div class="item-desc">chicken thigh, sweet chili, seasonal pickle</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">rock shrimp karaage</span><span class="item-price">24</span></div><div class="item-desc">tobanjan, chive</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">brussels sprouts</span><span class="item-price">11</span></div><div class="item-desc">sweet chili, lemon</div></div>
                </div>

                <div class="menu-section">
                    <h2>Makimono</h2>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> spicy crunchy</span><span class="item-price">16.5</span></div><div class="item-desc">tuna or salmon, cucumber, avocado, chili</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> zero sen</span><span class="item-price">17.5</span></div><div class="item-desc">yellowtail, avocado, shallot, cilantro</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">gyumaki</span><span class="item-price">18</span></div><div class="item-desc">australian wagyu, pickles, thai basil, kosho aioli</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">softshell crab</span><span class="item-price">18.5</span></div><div class="item-desc">pickled cucumber, cilantro, avocado, soy aioli</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">inari maki</span><span class="item-price">14</span></div><div class="item-desc">crispy tofu, avocado, red kosho</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> negihama</span><span class="item-price">12</span></div><div class="item-desc">yellowtail, green onion</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name"><span class="raw">‡</span> tekka</span><span class="item-price">11</span></div><div class="item-desc">bigeye tuna, tamari</div></div>
                </div>

                <div class="menu-section">
                    <h2>Okashi</h2>
                    <div class="menu-item"><div class="item-row"><span class="item-name">fried milk</span><span class="item-price">16</span></div><div class="item-desc">vanilla custard, salted fudge, toasted blondie</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">warm banana cake</span><span class="item-price">15</span></div><div class="item-desc">chicory caramel, buckwheat, white coffee ice cream</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">jasmine cream</span><span class="item-price">15</span></div><div class="item-desc">cilantro granita, pineapple, honey crumble</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">coconut tapioca</span><span class="item-price">14</span></div><div class="item-desc">pickled blueberry, hazelnut, lychee sorbet</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">seasonal sundae</span><span class="item-price">12</span></div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">black forest crepe cake</span><span class="item-price">15</span></div><div class="item-desc">chocolate, cherry, sakura leaves</div></div>
                    <div class="menu-item"><div class="item-row"><span class="item-name">fried milk ice cream pint <em>to-go</em></span><span class="item-price">12.5</span></div><div class="item-desc">salted fudge, toasted blondie, dulcey chocolate, cornflakes</div></div>
                </div>

            </div>

            <div class="menu-footnote">
                ‡ consuming raw or undercooked meats, poultry, seafood, shellfish, or eggs may increase your risk of foodborne illness.
            </div>

            </section>
        """)

        components.html(uchi_menu_html, height=600, scrolling=True)
