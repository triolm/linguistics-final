from shiny import ui, render, App
from outputs import *

app_ui = ui.page_fluid(
    ui.navset_tab(
        ui.nav(
            "Generate Text",
            ui.layout_sidebar(
                ui.panel_sidebar(
                    ui.input_selectize("sourcetext", "Source Text", ["shakespeare", "sherlock","riddleywalker"], selected=None, multiple=False, width=None),
                    ui.input_numeric("characters", "Characters", 50, min = 10, max = 7500),
                    ui.input_slider("n", "N", 1, 10, 3),
                    ui.input_checkbox_group("settings", "", ["ipa"], selected=None, inline=False, width=None),
                ),
                ui.panel_main(
                    ui.output_text("txt"),  
                ),
            ),
        ),
        ui.nav(
            "Generate Plot",
            ui.layout_sidebar(
                ui.panel_sidebar(
                    ui.input_selectize("plot_sourcetext", "Source Text", ["shakespeare", "sherlock","riddleywalker"], selected=None, multiple=False, width=None),
                    ui.input_slider("plot_n", "N", 1, 10, 3),
                    ui.input_slider("plot_nbars", "Number of bars", 5, 100, 20),
                    ui.input_checkbox_group("plot_settings", "", ["ipa", "omit_whitespace"], selected=None, inline=False, width=None),
                ),
                ui.panel_main(
                    ui.output_plot("plot"),
                ),
            ),
        ),
        ui.nav(
            "Generate Following Character Plot",
            ui.layout_sidebar(
                ui.panel_sidebar(
                    ui.input_selectize("children_sourcetext", "Source Text", ["shakespeare", "sherlock","riddleywalker"], selected=None, multiple=False, width=None),
                    ui.input_text("children_str", "Preceeding string", value="e"),
                    ui.input_slider("children_nbars", "Number of bars", 5, 100, 20),
                    ui.input_checkbox_group("children_settings", "", ["ipa", "omit_whitespace"], selected=None, inline=False, width=None),
                ),
                ui.panel_main(
                    ui.output_plot("children_plot"),
                ),
            ),
        ),
    ),
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        settings = input.settings()
        text = generate_text_from(input.sourcetext(),input.n(), input.characters(), ipa = "ipa" in settings)
        # print("regenerated text")
        return text
    @render.plot
    def plot():
        plot = None
        settings = input.plot_settings()
        plot = plot_ngrams_from(input.plot_sourcetext(), input.plot_n(), input.plot_nbars() , ipa = "ipa" in settings,omit_whitespace = "omit_whitespace" in settings)
        # print("generated plot")
        plot
    @render.plot
    def children_plot():
        plot = None
        settings = input.children_settings()
        print("eee")
        plot = plot_ngram_children_from(input.children_sourcetext(), input.children_str(), input.children_nbars() , ipa = "ipa" in settings,omit_whitespace = "omit_whitespace" in settings)
        # print("generated plot")
        plot

app = App(app_ui, server)