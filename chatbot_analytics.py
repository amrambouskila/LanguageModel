import nltk
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from typeguard import typechecked

matplotlib.use('Qt5Agg', force=True)
sns.set()


@typechecked
def word_analytics(sentences: list, width: int = 800, height: int = 400, background_color: str = 'white'):
    stop_words = set(stopwords.words('english'))
    text = [word for sentence in sentences for word in sentence.split(' ') if word not in stop_words]

    # Wordcloud
    tokens = nltk.word_tokenize(' '.join(text))
    processed_text = ' '.join(tokens)
    wordcloud = WordCloud(width=width, height=height, background_color=background_color).generate(processed_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # Word Distribution
    sequence_lengths = [len(sequence) for sequence in text]
    fig, ax = plt.subplots()
    ax.hist(sequence_lengths, bins=50)
    ax.set_xlabel('Sequence Length')
    ax.set_ylabel('Frequency')
    plt.show()


@typechecked
def plot_losses(train_info: dict):
    train_losses = train_info['train_losses']
    learning_rates = train_info['learning_rates']
    epochs = train_info['epochs']

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Loss', color='tab:blue')
    ax1.plot(epochs, train_losses, label='Training Loss', color='tab:blue')

    if len(train_info['val_losses']) > 0:
        ax1.plot(epochs, train_info['val_losses'], label='Validation Loss', color='tab:orange')
        ax1.legend(loc='best')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Learning Rate', color='tab:red')
    ax2.plot(epochs, learning_rates, label='Learning Rate', color='tab:red')

    ax1.tick_params(axis='y', labelcolor='tab:blue')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    fig.tight_layout()
    plt.title(f'Loss and Learning Rate over {max(train_info["epochs"])} Epochs')
    plt.show()
