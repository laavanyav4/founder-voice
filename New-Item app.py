from openai import OpenAI

client = OpenAI(api_key="your-api-key-here")

def analyze_style(posts):
    combined = "\n\n".join(posts)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert at analyzing writing styles."},
            {"role": "user", "content": f"""Analyze the writing style of these LinkedIn posts and describe:
1. Tone (formal/casual/bold/humble)
2. Average sentence length (short/medium/long)
3. Common phrases or patterns
4. Hook style (how posts start)
5. Ending style (how posts end)

Posts:
{combined}

Give a concise style profile."""}
        ]
    )
    return response.choices[0].message.content

def generate_post(style_profile, topic):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert LinkedIn ghostwriter."},
            {"role": "user", "content": f"""Write a LinkedIn post about: {topic}

Match this writing style exactly:
{style_profile}

Rules:
- Match the tone, sentence length, and patterns described
- Make it feel authentic, not AI-generated
- Keep it under 300 words
- No hashtags unless the style profile mentions them"""}
        ]
    )
    return response.choices[0].message.content

def main():
    print("\n=== Founder Voice Engine ===")
    print("Paste up to 5 LinkedIn posts to analyze the writing style.\n")
    
    posts = []
    for i in range(1, 4):
        print(f"Post {i} (paste it, then press Enter twice):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        post = " ".join(lines)
        if post:
            posts.append(post)
        
        if len(posts) >= 1:
            another = input("Add another post? (y/n): ")
            if another.lower() != 'y':
                break
    
    print("\nAnalyzing writing style...")
    style = analyze_style(posts)
    print("\n--- Style Profile ---")
    print(style)
    
    print("\n--- Generate Post ---")
    topic = input("\nWhat topic should the new post be about? ")
    
    print("\nGenerating post in their voice...\n")
    post = generate_post(style, topic)
    print("--- Generated Post ---")
    print(post)
    
    again = input("\nGenerate another post on a different topic? (y/n): ")
    if again.lower() == 'y':
        topic2 = input("New topic: ")
        post2 = generate_post(style, topic2)
        print("\n--- Generated Post ---")
        print(post2)

main()
