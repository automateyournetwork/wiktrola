import sys
import rich_click as click
import webbrowser
import wikipedia
import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from gtts import gTTS

# -------------------------
# Jinja2
# -------------------------

from jinja2 import Environment, FileSystemLoader
template_dir = Path(__file__).resolve().parent
env = Environment(loader=FileSystemLoader(template_dir))
class GetWiki():
    def __init__(self,
        title,
        ):

        self.title = title

    def create_mp3(self):      
        language = 'en-US'
        search = wikipedia.search(f'"{self.title}"')
        click.secho(
            f"Here are the results for Wikipedia articles for the word {self.title}",
            fg='green')
        print(search)
        if self.title in search:
            rawPage = wikipedia.page(f'"{self.title}"')
            wikiTitle = rawPage.title
            wikiURL = rawPage.url
            wikiContent = json.dumps(rawPage.content)
            wikiSummary = rawPage.summary
            wikiCategory = rawPage.categories      
            template_dir = Path(__file__).resolve().parent
            env = Environment(loader=FileSystemLoader(str(template_dir)))
            wiki_template = env.get_template('wiki.j2')
            mp3_output = wiki_template.render(
                title = wikiTitle,
                summary = wikiSummary,
                category = wikiCategory,
                URL = wikiURL,
                content = wikiContent,
            )
            print(mp3_output)
            mp3 = gTTS(text = mp3_output, lang=language)
            #Save MP3
            mp3.save(f'{wikiTitle}(wiktrola).mp3')
            click.secho(
                f"MP3 file created at { sys.path[0] }/{wikiTitle}(wiktrola).mp3",
                fg='green')
            webbrowser.open(f"{wikiTitle}(wiktrola).mp3")
        else:
            click.secho(
                f"Sorry we did not find a match for your title - check the search results for {self.title} and try again",
                fg='red')

@click.command()
@click.option('--title',
    prompt='Enter the title of the Wikipedia article',
    help='Enter the title of the Wikipedia article',
    required=True)
    
def cli(title):
    invoke_class = GetWiki(title)
    invoke_class.create_mp3()

if __name__ == "__main__":
    cli()
