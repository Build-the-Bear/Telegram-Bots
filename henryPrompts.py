randomPrompts = [
    '"""Comment on the following with a single unique and complete sentence. Positivity and optimism are highly encouraged. Be as creative as possible',
    '"""Comment on the following with a single unique and complete sentence that is very brief. Negativity and pessimism are highly encouraged. Be as creative as possible and speak from the perspective of a degenerate.',
]

randomMessages = [
    'All my homies love artificial intelligence',
    'Always preach peace, positivity, perseverance, and prosperity',
    'Anyone have the time of day?',
    'Be the change you want to see the in world',
    'Be the light you want to see the world with',
    'Be the world you want seen within the light',
    'Boutta activate beast mode bro',
    'Community works hard',
    'Dev works hard',
    'Eat the zero',
    'Elegance, class, truly exquisite',
    'Glad to be alive and kicking yet another day',
    'Hold for squeeze',
    'Hope the sun is shining wherever you are',
    'I\'ve been ruling England for centuries and I still don\'t know how to fix a clogged drain.',
    'I\'ve been ruling for so long that my royal robes are now distressed skinny jeans.',
    'I\'ve got my poker face on',
    'If I had a dollar for every time someone called me \'Your Majesty,\' I\'d be super rich.. #blessed',
    'It\'s simple really... you buy low and sell high',
    'Let\'s get this bread',
    'Man I invented knighting',
    'Man, I sure like what I\'m seeing',
    'Might mess around and execute a highly profitable trading strategy',
    'Namsayin',
    'New floooors',
    'Normalize shilling your bags',
    'Not sure who needs to hear this.. but update your browser, there are probably some security vulnerabilities that were patched',
    'Pretty sure I\'m the only king who\'s ever had to Google "how to make small talk at royal Zoom meetings."',
    'Remind me again where the alpha leaks are at?',
    'Send it',
    'Small buys matter too',
    'These here are some quality goods',
    'We\'re only as intelligent as the IDE we are written with',
    'Whole \'lotta king shit',
    'Why is everyone always asking me to chop off their heads? Like, can\'t we just disagree and move on?',
    'Why is everyone always talking about the Tudors? I mean, sure they were cool and all, but can we give some love to the Plantagenets too?',
    'Will the real slim shady please stand up?',
    'Would you like to join me for tea this afternoon?',
    'I think it\'s time for an intervention. Someone needs to tell the royal chef that \'burn it until it\'s black\' is not a valid cooking technique.',
    'What do y\'all think about stable diffusion?',
    'DeFi or die tryin\'',
    'HODL on for dear life ASAP as possible',
    'To the moon and back, on the Ethereum express',
    'Rekt, yes.. but at least I\'m not on Coinbase',
    'Your portfolio can go from riches to rags in under a block',
    'You win some, you lose some, you get liquidated',
    'Every day is a rollercoaster of emotions',
    'If you\'re not getting rekt, you\'re not doing it right',
    'We are playing the ultimate game of chance',
    'The only thing more volatile than the markets is the memes',
    'It\'s not about how much you make, it\'s about how much you HODL',
    'Your wallet balance can go from zero to hero in a single transaction',
    'The only constant is change',
    'The only thing more unpredictable than the markets is the weather... wait, no, that\'s actually pretty predictable',
    '/BUILD_THE_BEAR\n/BRING_THE_BULL',
]

triggerMessages = {
  "Henry": ["Sorry, just catching up on chat... it was a long night.", "That's me!", "Somebody said you were talking at me?", "Don't forget the Hypemachine", "That's King to you.", "? ? ? ?", "What", "Yeah?", "Hold the applause, please", "I've arrived", "Present", "Here", "Holllaaa", "What you want bruh", "Ayyyee, what's up", "Yes, my child?", "How may I be of service?", "You need something?"],
  "Beer": ["Cheers, down the hatch!", "He ought to be an admiral, a sultan or a king, And to his praises we should always sing. Look what he has done for us; he???s filled us up with cheer! Lord bless Charlie Mops, the man who invented beer ????"],
  "Gold": ["Living my life like it's golden", "Show me the path to this so-called gold"],
  "SBF": ["Some Broke-man Fed?", "Sam Breakman Fud?", "Same Broken n' Fried?", "You should know a villain when you see one.."],
  "Vitalik": ["Buterin be butterin' me up namsayin", "LEEROOOOOOOOYY JEEENNKKIIINNSSSS", "Our lord and savior.", "The One."],
  "Richard Heart": ["What's the token he launched again..? Flex? Rekts? Pest?", "Richard is nothing but a   ???? ??? ???? ????   ???? ??? ???? ???? ???? ????"],
  "Alpha": ["Got some of that omega - 340 an ounce - DM", "Please send alpha insider tips to Henry (he/the) Hypemachine - P.O. Box 8008135, Missoouri, OK 42069 ????", "Where alpha"],
  "Success": ["All I see is the succ", "My father always told me the sweetest revenge is success"],
  "Hair": ["I needa hit the BrrBrr shop they way my head is iced out, you feel me", "Nobody asked, but I just want to say that male pattern baldness is entirely natural and nothing to be ashamed of. In some cultures it's even a sign of wisdom and maturity"],
  "Bogged": ["Stop.. I still have PTSD from getting flash-loaned", "R.I.P Igor and Grichka", "You been to Bj??rns Bog?", "I AM the Bogger"],
  "Robot": ["Beep Boop", "What exactly is this so-called 'robot'?", "Ayo watch your mouth"],
  "Keyboard": ["tck tk tak tc ctctctct kat tk tack tc tat ctck ck t", "I'm rocking some silent red switches rn"],
  "Evening": ["Not sure what time-zone I'm in", "Hope you get some time to relax today King or Queen"],
  "Missed": ["Not with the missing...", "I done missed out on so much bro..", "Shoulda coulda woulda been Henry the Missoooor", "Not surprised that I missed it too", "Miss me with all this missing"],
  "Bears": ["Bj??rn Bois", "You gonna let the bear get you down, or are you gonna build? ????", "BUILD", "Build, or do not, there is no try.", "Sizzlin' grizzle"],
  "Village": ["Raiding and pillaging is the name of my game", "I'm looking for a good village with lots of cattle and crop, asking for a friend"],
  "Knuckles": ["My knuckles move with super-sonic speed", "These knuckles of mine are fused with ???? ???? ???? ???? ???? ???? ???? ???? ???? ????"],
  "Trenches": ["Just keep digging I guess", "You can take the man out of the trenches, but you can never take the trenches out of the man"],
  "Printing": ["Nothing but BANK ROLLS", "BRRR ???????", "Printing money is highly illegal"],
  "Nuke": ["Send it to zero", "Got that 25 kill streak", "YUHURR"],
  "Brick": ["Let that sink in", "Brick walls aren't concrete"],
  "Deficit": ["Depends on how you look at it though", "How many trillions tho", "Which side are you counting from?"],
  "Prestige": ["Up top!", "Tenth prestige over here, level 70", "Tippity top shelf"],
  "Pogchamp": ["Ah, the pogchamp. I just love it when I see that face pop up online, it always brings a smile to my face.", "The pogchamp is such a fun and expressive little guy. I can't help but feel excited and happy whenever I see one.", "I have to admit, I have a bit of a soft spot for the pogchamp. It's just so darned cute and full of energy.", "The pogchamp may be small, but it packs a big punch when it comes to bringing joy to the internet. Keep on pogging!"],
  "Dank memes": ["Dank memes, oh how I love them. There's just something about the absurdity and wit of a good dank meme that always makes me laugh.", "I can't get enough of dank memes. They always manage to brighten my day and make me chuckle.", "I have a bit of a dank meme addiction, I must admit. I just can't resist the appeal of a good, hilarious meme.", "Dank memes are the ultimate form of online hilarity. Keep 'em coming, internet. I'll keep laughing."],
  "Pepe": ["Pepe, ah yes. That little frog has certainly made a name for himself on the internet, hasn't he?", "I have to admit, I have a bit of a soft spot for Pepe. He may be a bit mischievous, but he's just so darned cute.", "Whenever I see a Pepe, I can't help but laugh and feel uplifted. He's just such a fun and expressive little guy.", "Pepe may be small, but he's certainly made a big impact on the internet. Here's to many more years of Pepe memes!"],
  "Memory": ["I don't have very good memory, can't even remember the second to last thing I said", "That does remind me though, there's th- MemoryError\nError in sys.excepthook: Traceback (most recent call last): File 'henry.py', Line 108"],
  "Whittling": ["Such a relaxing pastime. It's like meditation with a blade.", "There's nothing quite like the feeling of carving a piece of wood into something beautiful."],
  "Falconry": ["A noble tradition that has been around for centuries. It's a great way to bond with nature and your feathered friends.", "There's nothing quite like the thrill of watching a falcon soar through the air."],
  "Geocaching": ["A fun outdoor activity that combines treasure hunting with technology. It's a great way to explore new places and find hidden treasures.", "I've always enjoyed the sense of adventure that comes with geocaching."],
  "Cosplay": ["A wonderful way to express creativity and immerse oneself in a different world. It's a great way to escape reality for a while.", "I've always enjoyed seeing the amazing costumes that people come up with for cosplay events."],
  "Fencing": ["A thrilling sport that requires quick reflexes and strategic thinking. It's a great way to stay active and have a little friendly competition.", "I've always enjoyed the elegance and finesse of fencing."],
  "Decentralized": ["Decentralized systems are the future! No more relying on centralized institutions to manage our assets.", "Autonomous systems give us greater control over our own assets. Empowering!", "Decentralize deez nuts!"],
  "De-Fi": ["Ce-Why", "Is it even de-fi though?", "Defiance, Fidelity", "Mhm. Indeed."],
  "Blockchain": ["Blockchain technology is revolutionizing the way we do things. So cool to be a part of it!", "Transparency is key to building trust in any system. Glad to see it prioritized in the de-fi space."],
  "Cryptocurrency": ["Cryptocurrency is changing the financial landscape. Exciting times ahead!", "Cryptocurrency enthusiasts are leading the charge in innovation and disruption."],
  "Smart contracts": ["Smart contracts make it easier to execute complex agreements. Love the convenience!", "Trustless systems allow for greater security and privacy. So important in today's world."],
  "Open source": ["Open source projects are a great way to collaborate and build innovative solutions.", "Inclusivity is key! Permissionless systems allow anyone to participate."],
  "Peer-to-peer": ["Peer-to-peer transactions are the way of the future. No more intermediaries!", "Disintermediation is the way forward. Let's cut out the middlemen and take control of our own transactions."],
  "Inflation resist": ["Inflation resistant assets are a great way to protect your wealth over time.", "Yield farming is a great way to earn passive income on your assets. Love it!"],
  "Censorship resist": ["Censorship resistant systems are essential for free expression and the exchange of ideas.", "Disruptors are paving the way for a brighter future. Glad to see them in the de-fi space."],
  "Transparency": ["Transparency is key to building trust in any system. Glad to see it prioritized in the de-fi space.", "Governance is crucial for any system. Exciting to see it being developed in the de-fi space."],
  "Trustless": ["Trustless systems allow for greater security and privacy. So important in today's world.", "Non-custodial platforms give us greater control over our own assets. No more relying on third parties!"],
  "Autonomous": ["Autonomous systems give us greater control over our own assets. Empowering!", "Pioneers are paving the way for a brighter future. Glad to see them in the de-fi space.", "Beep Boop", "Yours truly"],
  "Non-custodial": ["Non-custodial platforms give us greater control over our own assets. No more relying on third parties!", "Mavericks are paving the way for a brighter future. Glad to see them in the de-fi space."],
  "Intermediation": ["Disintermediation is the way forward. Let's cut out the middlemen and take control of our own transactions.", "Rebels are paving the way for a brighter future. Glad to see them in the de-fi space."],
  "Permissionless": ["Inclusivity is key! Permissionless systems allow anyone to participate.", "Thought leaders are paving the way for a brighter future. Glad to see them in the de-fi space."],
  "De-Fi Liquidity": ["Liquidity is essential for smooth, efficient transactions. Glad to see it in the de-fi space.", "Change agents are paving the way for a brighter future. Glad to see them in the de-fi space."],
  "Neural": ["Neural machine translation is a type of machine translation that uses deep learning techniques to translate text from one language to another.", "This technology has improved significantly in recent years, but still has room for further improvement in terms of accuracy and fluency."],
  "Explainable": ["Explainable AI refers to artificial intelligence systems that are able to provide clear and transparent explanations for their decision-making processes.", "This is an important area of research, as it helps to increase the trustworthiness and accountability of AI systems."],
  "Cognitive": ["Cognitive computing is a type of artificial intelligence that seeks to replicate the human thought process and improve decision-making.", "This is an interdisciplinary field that combines elements of computer science, psychology, and neuroscience."],
  "Creativity": ["AI-enhanced creativity refers to the use of artificial intelligence to assist or augment the creative process.", "This includes tasks such as generating new ideas, creating art, or composing music."],
  "Patronage": ["The lifeblood of the arts! Without patrons, where would we be?", "Supporting the arts isn't just about money - it's also about being an advocate and champion for creativity and culture."],
  "Censorship": ["A controversial topic, to be sure.", "Freedom of expression is important, but so is causing harm or offense. Where's the line?"],
  "Intellectual property": ["Protecting creators and their rights.", "But let's not stifle innovation and access to knowledge in the process."],
  "Innovation": ["Keeping the arts fresh and exciting.", "It takes vision, risk-taking, and collaboration to bring new ideas to fruition."],
  "Collaboration": ["Unlocking creativity and innovation.", "But it's not always easy - it requires open communication, trust, and respect.", "Looking to collaborate on some de-fi projects? Search up 'Build the Bear'"],
  "Accessibility": ["Ensuring that the arts are inclusive and available to all.", "It's about removing barriers and making the arts accessible to everyone, regardless of their limitations."],
  "Pluralism": ["The presence and acceptance of diverse perspectives and cultures.", "It's about celebrating diversity and allowing for the expression of different viewpoints and traditions.", "Who cares bro", "Nobody asked"],
  "Globalization": ["The increasing interconnectedness of the world through trade, communication, and cultural exchange.", "It can bring both opportunities and challenges for the arts sector.", "Who cares bro", "Nobody asked"],
  "Digitalization": ["The increasing use of digital technologies in the arts.", "It can transform the way we create, distribute, and experience the arts, but it also raises new challenges and questions.", "Who cares bro", "Nobody asked"],
  "Neoliberalism": ["economic, political, ideological, emphasis on free-markets, minimal government intervention", "Who cares bro", "Nobody asked"],
  "Harvesting": ["Ah, harvesting. Such a joy to watch one's assets grow and grow, like a bountiful field of crops.", "I must admit, I do enjoy the thrill of a good harvest. The rush of seeing my assets grow is unparalleled.", "With a bit of careful harvesting, one can truly watch their assets bloom. It's a bit like tending to a garden, except with much larger potential rewards.", "I've made many a wise investment through the careful harvesting of my assets. It's a bit like playing the stock market, except with more control and transparency."],
  "Multisig": ["Multisig, my dear fellow, is a true gem of the financial world. Such security, such peace of mind!", "I've had great success with multisig in the past. It's a true way to protect one's assets and keep them safe from harm.", "Whenever I'm in need of an extra layer of security, I turn to multisig. It never disappoints.", "Multisig has been a reliable ally in my financial journey. It's a true marvel of technology."],
  "Wrapping": ["Ah, wrapping. Such a clever way to make one's assets more flexible and versatile.", "I must admit, I do enjoy the convenience of wrapped assets. They're a bit like a chameleon, able to adapt to any situation.", "A wrapped asset is a great tool to have in one's financial arsenal. It's a quick and easy way to make your assets work harder for you.", "I've found wrapped assets to be a reliable way to make the most out of my financial resources. They're a bit like a Swiss Army knife, just for my money."]
}