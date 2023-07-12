# Open and read the HTML file.
with open('updated.txt', 'rb') as file:
    html_content = file.read().decode(errors='replace')

# List of placeholders
placeholders    = [
'[linklink]',
'[benefit-title]',
'[introductory-hook]',
'[author-description]',
'[my-authors-opinion]',
'[product-target-audience]',
'[target-audience1]',
'[target-audience2]',
'[target-audience3]',
'[target-audience4]',
'[target-audience5]',
'[personal-results-description]',
'[product-benefit1]',
'[product-name]',
'[product-method-benefit]',
'[product-method-description]',
'[product-beneficiary-description]',
'[example-company1]',
'[example-company2]',
'[example-company3]',
'[example-company4]',
'[transition-to-key-points]',
'[key-point1]',
'[key-point2]',
'[benefit-examples-title]',
'[benefit-example1]',
'[benefit-example2]',
'[benefit-example3]',
'[benefit-example4]',
'[benefit-example5]',
'[conclusion-formula]',
'[transition-to-stats]',
'[statistic1]',
'[transition-to-steps]',
'[transition-to-benefits]',
'[benefit-point1]',
'[benefit-explanation1]',
'[benefit-usecase1]',
'[transition-to-benefit2]',
'[benefit-point2]',
'[benefit-explanation2]',
'[benefit-usecase2]',
'[step1-title]',
'[step1-description1]',
'[step1-description2]',
'[step1-description3]',
'[transition-to-step1-topics]',
'[step1-topic1]',
'[step1-topic2]',
'[step1-topic3]',
'[step1-topic4]',
'[step1-topic5]',
'[step2-title]',
'[step2-description1]',
'[step2-description2]',
'[step2-description3]',
'[step3-title]',
'[step3-description1]',
'[step3-description2]',
'[transition-to-step3-topics]',
'[step3-topic1]',
'[step3-topic2]',
'[step3-topic3]',
'[step3-topic4]',
'[step3-topic5]',
'[step3-conclusion1]',
'[step3-conclusion2]',
'[step3-elaboration1]',
'[step3-elaboration2]',
'[step4-title]',
'[transition-to-step4]',
'[transition-to-step4-explanation]',
'[step4-explanation-conclusion]',
'[step4-topic1]',
'[step4-topic2]',
'[step4-topic3]',
'[step4-topic4]',
'[step4-topic5]',
'[4-steps-conclusion]',
'[putting-it-all-together-title]',
'[transition-to-system-benefits]',
'[system-benefit1]',
'[system-benefit2]',
'[system-benefit3]',
'[system-benefit4]',
'[system-benefit5]',
'[product-name-title]',
'[transition-to-ethics]',
'[unethical-point1]',
'[unethical-elaboration1]',
'[unethical-point2]',
'[unethical-elaboration2]',
'[transition-to-ethical]',
'[ethical-point1]',
'[ethical-elaboration1]',
'[ethical-point2]',
'[ethical-elaboration2]',
'[how-to-start-title]',
'[how-to-start-paragraph1]',
'[how-to-start-paragraph2]',
'[transition-to-bonus]',
'[bonus-offer1]',
'[bonus-offer2]',
'[bonus-offer3]',
'[bonus-offer4]',
'[proof-section-title]',
'[bonus-section]',
'[bonus-option1]',
'[bonus-option2]',
'[bonus-option3]',
'[recommendation-paragraph]',
'[special-bonus]',
'[bonus-join-now-sentence]',
'[bonus-join-now-paragraph1]',
'[bonus-join-now-paragraph2]',
'[bonus-join-now-paragraph3-action-text]',
'[review-section-title]',
'[comment5]',
'[response5]',
'[comment4]',
'[response4]',
'[comment3]',
'[response3]',
'[comment2]',
'[response2]',
'[comment1]',
'[response1]',
'[benefit-title]'	,
'[introductory-hook]',
'[benefit-point1]', 
'[benefit-point2]'	,
'[statistic1]'	,
'[product-name]'	,
'[product-method-description]'	,
'[product-name-title]'	,
'[img-alt-1]'	,
'[img-alt-2]'	,
'[img-alt-3]'	,
'[img-alt-4]'	,
'[img-alt-5]'	
]

# List of replacements
replacements = [
    'https://07caegk5r7hhpu0k7j42q8w58q.hop.clickbank.net/?tid=mysticguard',

"Discover the Power of MysticGuard Sketch: Unlock Genuine Relationships and Protection"	,
"Are you tired of falling into toxic relationships? Do you wish to shield yourself from emotional harm? Read on."	,
"As an experienced copywriter and marketing expert, I've seen countless individuals struggle with trust and emotional well-being. That's why I want to introduce you to a game-changing solution."	,
"In my opinion, MysticGuard Sketch is a revolutionary tool that can transform your life by providing valuable insights and protecting you from manipulative individuals."	,
"MysticGuard Sketch is perfect for individuals who value their emotional well-being and seek genuine relationships."	,
"Those who have experienced heartaches and distress from toxic relationships."	,
"Individuals looking to navigate social interactions with confidence and peace of mind."	,
"Business professionals who want to evaluate their connections and forge authentic relationships."	,
"Parents concerned about protecting their loved ones from harmful influences."	,
"Anyone who desires personal growth and a life free from manipulation."	,
"Personally, I have witnessed the transformative power of MysticGuard Sketch. It has helped me avoid toxic individuals and establish meaningful connections."	,
"Identify manipulative individuals before meeting them face to face."	,
"MysticGuard Sketch"	,
"Safeguard yourself from emotional harm and navigate social interactions with confidence."	,
"MysticGuard Sketch provides meticulously detailed sketches of individuals, enabling you to recognize potential red flags and establish healthier relationships."	,
"Let MysticGuard Sketch be your guide, protecting you from manipulative individuals and empowering you to make proactive decisions."	,
"Maria's Success Inc."	,
"Trustworthy Connections Ltd."	,
"Safe and Secure Enterprises"	,
"Guarded Relationships Co."	,
"Now let's delve into the key points that make MysticGuard Sketch truly remarkable."	,
"MysticGuard Sketch provides a detailed portrayal of an individual's true nature and character."	,
"The sketches help you sever ties with manipulative individuals, protecting your life from distress and problems."	,
"Real-Life Examples of MysticGuard Sketch in Action"	,
"Maria Beltran avoided a manipulative individual, saving her professional reputation."	,
"Martha Beth Stein protected her daughter from harmful influences with the guidance of MysticGuard Sketch."	,
"John Smith discovered a potential red flag through the sketch, avoiding a toxic relationship."	,
"Sarah Johnson used MysticGuard Sketch to evaluate business connections and establish genuine partnerships."	,
"James Anderson experienced personal growth and built healthier relationships after using MysticGuard Sketch."	,
"In conclusion, MysticGuard Sketch offers a unique opportunity to shield yourself from manipulation and embrace a life filled with genuine connections and personal growth."	,
"But let's look at some astonishing statistics that highlight the effectiveness of MysticGuard Sketch."	,
"Over 90% of users reported improved emotional well-being and the ability to identify toxic individuals."	,
"Now, let me walk you through the steps to embark on your journey with MysticGuard Sketch."	,
"But before we dive into the steps, let's revisit the key benefits you'll experience with MysticGuard Sketch."	,
"Proactively protect yourself from emotional harm and toxic relationships."	,
"By receiving detailed sketches and insights, you'll have the power to recognize potential red flags and make informed decisions."	,
"Imagine avoiding a manipulative person and saving yourself from heartache and distress."	,
"Now let's explore another incredible benefit MysticGuard Sketch offers."	,
"Establish genuine connections and navigate social interactions with confidence."	,
"The sketches provide you with insights into an individual's true nature, enabling you to forge healthier relationships and build trust."	,
"Imagine evaluating professional connections and building partnerships based on genuine trust and compatibility."	,
"Step 1: Visit the Official MysticGuard Sketch Website"	,
"Go to the official website by clicking the link provided."	,
"Choose your preferred package: 1 sketch, 2 sketches, or 3 sketches."	,
"Complete the purchase process securely and efficiently."	,
"Now, let's explore some topics you'll find on the official website to make an informed decision."	,
"Detailed information about the process and how the sketches are created."	,
"Testimonials from satisfied customers who have experienced the benefits firsthand."	,
"Frequently Asked Questions to address any concerns or doubts you may have."	,
"Money-back guarantee and customer support details to ensure your satisfaction."	,
"Secure payment options and data protection measures for a worry-free purchase."	,
"Step 2: Receive Your Personalized MysticGuard Sketch"	,
"Within a few days of your purchase, you'll receive a meticulously detailed sketch via email."	,
"Carefully examine the sketch and take note of the intricate details, expressions, and facial features depicted."	,
"The sketch provides a visual representation of the person you should be cautious of, empowering you to make informed decisions."	,
"Step 3: Explore the MysticGuard Sketch Website for In-Depth Information"	,
"Visit the MysticGuard Sketch website and navigate through the wealth of information provided."	,
"Discover the key features, benefits, and testimonials that further reinforce the effectiveness of MysticGuard Sketch."	,
"Let's delve into some important topics you'll find on the website to enhance your understanding."	,
"How the sketches are created: Insights into the meticulous process employed by psychics Zela and Ram."	,
"Real-life testimonials: Stories from satisfied customers who have experienced the power of MysticGuard Sketch firsthand."	,
"Frequently Asked Questions: Find answers to common queries and address any doubts or concerns."	,
"Money-back guarantee and customer support: Assurance of a risk-free purchase and access to dedicated assistance."	,
"Data protection and privacy: Details on how your personal information is safeguarded during the process."	,
"By exploring these topics, you'll gain deeper insights into the authenticity and effectiveness of MysticGuard Sketch."	,
"It will help you make an informed decision and ensure your satisfaction with the product."	,
"The detailed process of sketch creation showcases the expertise and accuracy of psychics Zela and Ram."	,
"Real-life testimonials validate the positive impact of MysticGuard Sketch on individuals' lives, building trust in its efficacy."	,
"Step 4: Experience the Transformative Power of MysticGuard Sketch"	,
"Now, let's uncover the incredible benefits you'll enjoy by embracing MysticGuard Sketch."	,
"But before that, let's understand why this system stands out from other alternatives in the market."	,
"By providing detailed sketches and personalized insights, MysticGuard Sketch offers a comprehensive solution for protecting your emotional well-being and fostering genuine connections."	,
"Accurate and detailed sketches: Recognize potential red flags and avoid toxic individuals."	,
"Insights into true nature and character: Establish meaningful connections based on genuine compatibility."	,
"Proactive decision-making: Shield yourself from emotional harm and make informed choices."	,
"Enhanced personal safety: Navigate social interactions confidently with the power of insights."	,
"Uncover hidden intentions: Protect yourself from manipulative individuals who may harm your well-being."	,
"By following these four steps, you'll embark on a transformative journey towards genuine relationships and emotional well-being."	,
"Putting it All Together: The System's Benefits at a Glance"	,
"Now, let's summarize the key benefits you'll experience by embracing MysticGuard Sketch."	,
"Protection from emotional harm and toxic relationships."	,
"Confidence in navigating social interactions and establishing genuine connections."	,
"Proactive decision-making based on insights into individuals' true nature."	,
"Personal safety and avoidance of manipulative individuals."	,
"Uncovering hidden intentions and safeguarding your emotional well-being."	,
"Introducing MysticGuard Sketch: A Path to Genuine Relationships and Emotional Well-being"	,
"Now, let's address the ethics surrounding MysticGuard Sketch."	,
"Some might question the ethical implications of using psychic insights for personal decision-making."	,
"However, it's important to remember that MysticGuard Sketch empowers individuals to protect themselves from potential harm and make informed choices."	,
"The ethicality of using psychic abilities is subjective, but the testimonials and positive experiences of users speak for themselves."	,
"Psychics Zela and Ram have honed their skills to genuinely help individuals, and their intentions are focused on promoting emotional well-being."	,
"Now, let's consider the ethical perspective of using MysticGuard Sketch."	,
"MysticGuard Sketch respects individuals' autonomy and empowers them to make decisions based on insights."	,
"It promotes self-awareness, personal growth, and protection from manipulation, all of which align with ethical principles."	,
"The ethicality of seeking guidance and support is a personal choice, and MysticGuard Sketch offers a tool for individuals seeking such assistance."	,
"It enables users to foster genuine connections and establish healthier relationships, which are essential aspects of ethical interpersonal interactions."	,
"How to Start Your MysticGuard Sketch Journey"	,
"To begin your transformative journey with MysticGuard Sketch, follow these simple steps."	,
"Visit the official MysticGuard Sketch website and choose your preferred package."	,
"But before you get started, let me introduce you to the exciting bonus offers available."	,
"Bonus #1: Exclusive access to a private community of like-minded individuals seeking personal growth and genuine connections."	,
"Bonus #2: A comprehensive guide on recognizing and avoiding toxic relationships in different areas of your life."	,
"Bonus #3: Weekly inspirational emails from psychics Zela and Ram to support you on your journey."	,
"Bonus #4: Personalized guidance on interpreting the sketches and making the most of the insights provided."	,
"Real Proof of MysticGuard Sketch's Effectiveness"	,
"Let's take a closer look at the bonus options available to enhance your MysticGuard Sketch experience."	,
"Option #1: Join our exclusive webinars conducted by renowned relationship experts."	,
"Option #2: Access to additional sketch interpretations for a deeper understanding of the individuals you encounter."	,
"Option #3: Personal coaching sessions with psychics Zela and Ram to guide you through your journey."	,
"Based on my experience and the overwhelming positive feedback from satisfied users, I wholeheartedly recommend MysticGuard Sketch."	,
"Special Bonus: Limited-time offer! Receive a free digital copy of 'The Art of Authentic Connections' by renowned author Jane Doe."	,
"Join now and take advantage of these incredible bonuses to enhance your MysticGuard Sketch experience."	,
"To claim your bonuses and start your transformative journey, visit the official MysticGuard Sketch website."	,
"Select your preferred package and gain instant access to the bonuses, ensuring a comprehensive and rewarding experience."	,
"Take action now and embark on a life-changing path with MysticGuard Sketch!"	,
"MysticGuard Sketch: A Review of its Transformative Power"	,
"I was skeptical at first, but after trying MysticGuard Sketch, I'm amazed by its accuracy. It has truly helped me navigate my relationships with confidence."	,
"Thank you for sharing your experience! We're thrilled that MysticGuard Sketch has had a positive impact on your life."	,
"The sketches provided by MysticGuard are incredibly detailed. It's like having a glimpse into someone's true nature even before meeting them. Highly recommended!"	,
"We appreciate your feedback! The detailed sketches are a key feature of MysticGuard Sketch, enabling users to make informed decisions and protect themselves."	,
"MysticGuard Sketch has been a game-changer for me. It helped me identify a toxic person in my life and avoid further heartache. I can't thank you enough!"	,
"We're delighted to hear that MysticGuard Sketch has made a positive difference in your life. Thank you for sharing your story with us."	,
"I was hesitant to try MysticGuard Sketch at first, but I'm so glad I did. It has given me the confidence to trust my instincts and build healthier relationships."	,
"We understand your initial hesitation, and we're thrilled that MysticGuard Sketch has exceeded your expectations. Thank you for sharing your experience!"	,
"I was curious about MysticGuard Sketch, so I decided to give it a try. The insights provided were eye-opening and helped me avoid potential trouble. Highly recommend!"	,
"Thank you for sharing your positive experience with MysticGuard Sketch! We're glad it has helped you make proactive decisions and avoid unnecessary difficulties."	,
"Unlocking Genuine Relationships and Emotional Well-being with MysticGuard Sketch"	,
"Are you tired of being blindsided by toxic relationships? Discover how MysticGuard Sketch can empower you to navigate social interactions with confidence."	,
"Recognize potential red flags and protect yourself from emotional harm and distress."	,
"Establish genuine connections based on insights into individuals' true nature and character."	,
"Studies show that over 90% of users report improved emotional well-being and the ability to identify toxic individuals with MysticGuard Sketch."	,
"MysticGuard Sketch"	,
"MysticGuard Sketch provides meticulously detailed sketches and personalized insights, empowering individuals to make informed decisions and navigate relationships effectively."	,
"Unveiling MysticGuard Sketch: Transforming the Way You Approach Relationships"	,
"Person holding MysticGuard Sketch sketch"	,
"MysticGuard Sketch detailed sketch example"	,
"Two individuals connecting with MysticGuard Sketch guidance"	,
"MysticGuard Sketch testimonial quote from satisfied customer"	,
"MysticGuard Sketch package options with bonuses"	
    
    ]

# Check if both lists have same length
if len(placeholders) != len(replacements):
    print(len(placeholders))
    print(len(replacements))

    raise ValueError("Both lists should have same number of elements")

# Replace placeholders with replacements
for i in range(len(placeholders)):
    if(placeholders[i] in html_content ):
        html_content = html_content.replace(placeholders[i], replacements[i])

# Write the new HTML to a file.
with open('updated.html', 'wb') as file:
    file.write(html_content.encode())
 


with open('top-recomendations updated.txt', 'rb') as file:
    html_content = file.read().decode(errors='replace')

# Replace placeholders with replacements
for i in range(len(placeholders)):
    if(placeholders[i] in html_content ):
        html_content = html_content.replace(placeholders[i], replacements[i])


# Write the new HTML to a file.
with open('article.html', 'wb') as file:
    file.write(html_content.encode())
