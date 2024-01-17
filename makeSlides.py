#!/usr/bin/env python3

import os
from pptx import Presentation
from pptx.util import Inches, Pt

# Create a presentation object
prs = Presentation()

# Define slide titles and content

slides_content = [
    ("Who Am I?", [
        "Platform Architect at Codence",
        "Conversational-but-not-fluent in Python, JavaScript, C#, etc.",
        "Enthusiastic about clean code and efficient coding practices"
    ], "This slide sets the tone for the presentation, establishing credibility and rapport with the audience."),
    
    ("Who is This Talk For?", [
        "Developers at the beginner to intermediate level",
        "Emphasis on readability and maintainability of code",
        "Introduction of guard clauses and single-pass loops"
    ], "This slide helps attendees understand whether the content is relevant to them and what they can expect to learn."),
    
    ("Understanding Guard Clauses", [
        "A guard clause checks if a script should continue or exit early",
        "Benefits of preventing deeply nested code",
        "Further Reading: Links to Codementor and Wikipedia articles"
    ], "The key function and advantages of using guard clauses are laid out here to familiarize the audience with the concept."),
    
    ("Single-Pass Loops: Simplifying Code Execution", [
        "The concept of single-pass loops as a robust structure",
        "How it works hand-in-hand with guard clauses",
        "Advantages over traditional methods and further resources"
    ], "This slide dives into the concept of single-pass loops, helping the audience understand how it can be used to emulate try-catch behavior."),
    
    ("Control Structures: IF vs GUARD Clauses", [
        "Nested IF statements vs. guard clauses",
        "DEMO1: Showing real-world benefits of guard clauses over IF for enhancing code quality"
    ], "This slide provides concrete examples to show the practical advantages of using guard clauses in everyday coding."),
    
    ("Single-Pass Loop Strategy: 'Exit Loop If' for Control Flow", [
        "Clarification on using 'Exit Loop If' within single-pass loops",
        "Placement of the singular 'Exit Script' in the 'finally' section",
        "DEMO2: Scripted example showcasing effective control flow management"
    ], "Here, the focus shifts to the correct application of 'Exit Loop If' and 'Exit Script' in a single-pass loop, with a scenario illustrating their roles."),
    
    ("Balancing Simplicity and Robustness in Control Flow", [
        "Recap of best practices for 'Exit Loop If' and 'Exit Script'",
        "Pros and Cons: The balance between easy-to-manage and comprehensive error handling",
        "Discussion of maintaining clear intent in scripting for reliability"
    ], "This slide pulls together the key points from earlier discussions, leaving the audience with clear actionable insights on managing script control flow.")
]

# Function to add a slide to the presentation
def add_slide(title, content, note):
    # Add a title and content slide
    slide_layout = prs.slide_layouts[1]  # 0 is for title slide, 1 for title and content
    slide = prs.slides.add_slide(slide_layout)
    title_placeholder = slide.shapes.title
    content_placeholder = slide.placeholders[1]
    
    # Set title
    title_placeholder.text = title
    
    # Add content as bullet points
    for i, bullet_point in enumerate(content):
        p = content_placeholder.text_frame.add_paragraph()
        p.text = bullet_point
        p.font.size = Pt(18)
        if i == 0:  # for the first bullet point
            p.level = 0
        else:  # for sub bullet points
            p.level = 1
    
    # Add notes to the slide
    notes_slide = slide.notes_slide
    notes_text_frame = notes_slide.notes_text_frame
    notes_text_frame.text = note

# Generate all slides
for slide_title, slide_content, slide_note in slides_content:
    add_slide(slide_title, slide_content, slide_note)

# Save the presentation
prs.save('presentation.pptx')

print("Presentation created successfully!")

# Open the presentation
os.system("open presentation.pptx")  # for macOS