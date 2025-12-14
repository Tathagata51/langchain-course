import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def main():
    print("Hello From Langchain")
    information = '''
    Rabindranath Thakur FRAS (Bengali: [roˈbindɾonatʰ ˈʈʰakuɾ];[1] anglicised as Rabindranath Tagore /rəˈbɪndrənɑːt təˈɡɔːr/ ⓘ; 7 May 1861[2] – 7 August 1941[3]), also known by his pseudonym Bhanusimha (Sun Lion) was a Bengali polymath (poet, writer, playwright, composer, philosopher, social reformer, and painter) of the Bengal Renaissance period.[4][5][6] In 1913, Tagore became the second non-European to win a Nobel Prize in any category, and also the first lyricist to win the Nobel Prize in Literature.[7] He has written the national anthems of India and Bangladesh.
    He reshaped Bengali literature and music as well as Indian art with Contextual Modernism in the late 19th and early 20th centuries. He was the author of the "profoundly sensitive, fresh and beautiful" poetry of Gitanjali.[8] Tagore's poetic songs were viewed as spiritual and mercurial; his elegant prose and magical poetry were widely popular in the Indian subcontinent.[9] He was a fellow of the Royal Asiatic Society. Referred to as "the Bard of Bengal",[10][5][6] Tagore was known by the sobriquets Gurudev, Kobiguru, and Biswokobi.[a]
    A Bengali Brahmin from Calcutta with ancestral gentry roots in Jessore and Bardhaman districts, Tagore wrote poetry as an eight-year-old.[12][13] At the age of sixteen, he released his first substantial poems under the pseudonym Bhānusiṃha ("Sun Lion"), which were seized upon by literary authorities as long-lost classics.[14] By 1877 he graduated to his first short stories and dramas, published under his real name. As a humanist, universalist, internationalist, and ardent critic of nationalism,[15] he denounced the British Raj and advocated independence from Britain. As an exponent of the Bengal Renaissance, he advanced a vast canon that comprised paintings, sketches and doodles, hundreds of texts, and some two thousand songs; his legacy also endures in his founding of Visva-Bharati University.[16][17]
    Tagore modernised Bengali art by spurning rigid classical forms and resisting linguistic strictures. His novels, stories, songs, dance dramas, and essays spoke to topics political and personal. Gitanjali (Song Offerings), Gora (Fair-Faced), and Ghare-Baire (The Home and the World) are his best-known works. His poetry, short stories, and novels were both praised and criticised for their lyricism, colloquial tone, naturalism, and philosophical introspection. His compositions were chosen by two nations as national anthems: India's "Jana Gana Mana" and Bangladesh's "Amar Shonar Bangla". The Sri Lankan national anthem was also inspired by his work.[18] His song "Banglar Mati Banglar Jol" has been adopted as the state anthem of West Bengal.
    '''
    summery_template = '''Given the {information} about a person, I want you to create:
    1. A short summary.
    2. two interesting facts about them.
    '''
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summery_template
    )
    llm = ChatGoogleGenerativeAI(
        temperature=0, model="models/gemini-2.5-flash-lite")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response)


if __name__ == "__main__":
    main()
