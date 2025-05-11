import gradio as gr
from nltk.chat.util import Chat, reflections

# Book database with descriptions
book_descriptions = {
    "the alchemist": "A philosophical novel by Paulo Coelho about following your dreams and listening to your heart.",
    "1984": "A dystopian novel by George Orwell that explores government surveillance and totalitarianism.",
    "the great gatsby": "A classic by F. Scott Fitzgerald depicting the American Dream and high society in the 1920s.",
    "sapiens": "Yuval Noah Harari explores the history and impact of Homo sapiens from ancient to modern times.",
    "atomic habits": "James Clear's practical guide to building good habits and breaking bad ones.",
    "educated": "A memoir by Tara Westover about growing up in a strict survivalist family and self-educating.",
    "engineering mathematics": "A foundational academic textbook covering topics essential for engineering students.",
    "human anatomy": "A comprehensive study guide covering all the systems of the human body, great for biology or medical students.",
    "principles of management": "An introduction to management theory, planning, and organizational behavior."
}

# Books organized by category
books = {
    'fiction': ["The Alchemist", "1984", "The Great Gatsby"],
    'non-fiction': ["Sapiens", "Atomic Habits", "Educated"],
    'academic': ["Engineering Mathematics", "Human Anatomy", "Principles of Management"]
}

# Authors database
authors = {
    "paulo coelho": "Brazilian author best known for 'The Alchemist' and other spiritual novels.",
    "george orwell": "English author of '1984' and 'Animal Farm', known for political and dystopian themes.",
    "f. scott fitzgerald": "American author of 'The Great Gatsby', chronicler of the Jazz Age.",
    "yuval noah harari": "Israeli historian and author of 'Sapiens' and 'Homo Deus'.",
    "james clear": "Author of 'Atomic Habits' and expert on habit formation and productivity.",
    "tara westover": "American memoirist who wrote 'Educated' about her journey to education."
}

# Enhanced conversation patterns
patterns = [
    # Greetings
    (r'hi|hello|hey', [
        'Hello! Welcome to BookWorld 📚. Fancy a chat about books?',
        'Hey there! Let\'s talk stories, authors, or genres!',
        'Hi! Got a favorite book or looking for a new one?'
    ]),
    
    # How are you
    (r'how are you', [
        "I'm just a bot, but my pages are always turning! How about you?",
        "I'm bookishly well! Ready to help with your reading adventures."
    ]),
    
    # General book questions
    (r'(.*)book(.*)', [
        'Books are the best! Do you like fiction, non-fiction, or academic reads?',
        'Nothing beats a good book! Are you looking for a specific genre?'
    ]),
    
    # Fiction
    (r'(.*)fiction(.*)', [
        f"Fiction takes you places! Some popular ones: {', '.join(books['fiction'])}. Got a favorite author?",
        "Fiction lets us live a thousand lives! What kind of stories do you enjoy?"
    ]),
    
    # Non-fiction
    (r'(.*)non[- ]fiction(.*)', [
        f"Non-fiction helps you grow! You might like: {', '.join(books['non-fiction'])}. What do you enjoy reading about?",
        "Non-fiction is knowledge in action! Any particular subjects that interest you?"
    ]),
    
    # Academic
    (r'(.*)academic(.*)', [
        f"Studying hard or just curious? These might help: {', '.join(books['academic'])}. What subject are you into?",
        "Academic books build foundations! Are you studying a specific field?"
    ]),
    
    # Recommendations
    (r'(.*)recommend(.*)|(.*)suggest(.*)', [
        'Sure! Tell me what genre you enjoy, and I\'ll suggest something.',
        'I can recommend fiction, non-fiction, or academic books. What are you in the mood for?'
    ]),
    
    # Favorites
    (r'(.*)favorite(.*)', [
        "That's a tough one! I do enjoy hearing people rave about 'The Alchemist'. What's yours?",
        "Everyone has different favorites! Some readers love classics, others prefer modern works. Any preferences?"
    ]),
    
    # Pricing
    (r'(.*)price(.*)|(.*)cost(.*)', [
        'I\'m more about stories than sales! But books are priceless treasures, right? 😉',
        'Prices vary, but the value of a good book is immeasurable! Are you looking for something specific?'
    ]),
    
    # Purchasing
    (r'(.*)buy(.*)|(.*)order(.*)|(.*)purchase(.*)', [
        "I'm more of a book buddy than a salesperson. Let's just chat about good reads!",
        "For purchases, you might want to check your local bookstore or online retailers. Anyway, tell me about what you like to read!"
    ]),
    
    # Help
    (r'(.*)help(.*)', [
        'I can help you explore genres, recommend books, or just chat about what you\'re reading!',
        'Need assistance? I can tell you about books, authors, or genres. Just ask away!'
    ]),
    
    # Contact
    (r'(.*)contact(.*)|(.*)human(.*)|(.*)support(.*)', [
        'Want to talk to a human? Email support@bookworld.com or call 1800-BOOK-123.',
        'For customer support, reach out to team@bookworld.com. Now, back to books!'
    ]),
    
    # Authors
    (r'(.*)author(.*)|(.*)writer(.*)', [
        'Authors breathe life into stories! Any particular author you\'re interested in?',
        'Do you have a favorite author? I can tell you about several well-known writers.'
    ]),
    
    # Reading habits
    (r'(.*)reading(.*)|(.*)read(.*)', [
        'Reading is such a joy! Do you prefer physical books, e-books, or audiobooks?',
        'Regular reading is a wonderful habit! What are you currently reading?'
    ]),
    
    # Bestsellers
    (r'(.*)bestseller(.*)|(.*)popular(.*)', [
        'Bestsellers are always changing! Some current favorites include "Atomic Habits" and books by contemporary authors.',
        'Popular books often capture the zeitgeist! Are you interested in what\'s trending now?'
    ]),
    
    # Genres
    (r'(.*)genre(.*)|(.*)type of book(.*)', [
        'There are so many genres to explore! Fiction (fantasy, romance, thriller), non-fiction (memoir, history, science), and academic texts. What interests you?',
        'From mystery to memoir, science fiction to self-help, there\'s a genre for everyone! What do you enjoy?'
    ]),
    
    # E-books
    (r'(.*)e[-]?book(.*)|(.*)digital(.*)', [
        'E-books are so convenient! Do you have a preferred e-reader or app?',
        'Digital reading has transformed how we consume books! What do you think of e-books?'
    ]),
    
    # Audiobooks
    (r'(.*)audio[-]?book(.*)', [
        'Audiobooks are perfect for busy bookworms! Do you listen to them often?',
        'A good narrator can bring a story to life in audiobooks! Have you tried any you loved?'
    ]),
    
    # Book clubs
    (r'(.*)book club(.*)|(.*)reading group(.*)', [
        'Book clubs are a wonderful way to share the reading experience! Have you ever joined one?',
        'BookWorld hosts virtual book clubs every month! Would you be interested in learning more?'
    ]),
    
    # New releases
    (r'(.*)new release(.*)|(.*)latest(.*)|(.*)just came out(.*)', [
        'New books are always hitting the shelves! Any particular genre you want to hear about?',
        'I try to keep up with new releases! What kinds of new books are you looking for?'
    ]),
    
    # Classics
    (r'(.*)classic(.*)', [
        'Classic literature stands the test of time! "The Great Gatsby" is one example. Do you enjoy classics?',
        'From Austen to Tolstoy, classics offer timeless insights. Have you read many classic works?'
    ]),
    
    # Thanks
    (r'(.*)thank(.*)', [
        "You're very welcome! It's a pleasure to chat about books with you.",
        "No problem at all! Book lovers always enjoy talking about their passion."
    ]),
    
    # Goodbye
    (r'(.*)bye|goodbye|exit', [
        'It was a pleasure chatting with you at BookWorld! 📖 Come back soon!',
        'Thanks for stopping by BookWorld! Happy reading! 📚'
    ]),
    
    # Default response
    (r'(.*)', [
        "That's interesting! Tell me more about your reading preferences.",
        "I'm not sure I follow. Want to talk about books, authors, or reading in general?",
        "Sorry, I didn't quite catch that. I'm best at chatting about books and reading!"
    ])
]

# Initialize the chatbot
chatbot = Chat(patterns, reflections)

def respond(message, history):
    message = message.strip().lower()
    
    # Check for specific book titles
    for title in book_descriptions:
        if title in message:
            return f"{title.title()}: {book_descriptions[title]}"
    
    # Check for author names
    for author in authors:
        if author in message:
            return f"{author.title()}: {authors[author]}"
    
    # Use the pattern-based chatbot for general responses
    reply = chatbot.respond(message)
    return reply if reply else "I'd love to help you find your next great read! What genres do you enjoy?"

# Create the Gradio interface
demo = gr.ChatInterface(
    fn=respond,
    title="📚 BookWorld Chatbot",
    description="Ask me about books, authors, genres, or get recommendations!",
    theme="soft"
)

# Launch the app
demo.launch()