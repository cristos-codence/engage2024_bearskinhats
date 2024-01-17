#!/usr/bin/env python3

import os
from pptx import Presentation
from pptx.util import Inches

# Create a presentation object
prs = Presentation()

# Slide Titles and Content
slides_content = [
    ("Who Am I?", [
        "Platform Architect at Codence",
        "Conversational-but-not-fluent in Python, JavaScript, C#, etc.",
        "Passionate about efficient coding practices"
    ]),
    ("Who is This Talk For?", [
        "Beginner to Intermediate Level Developers",
        "Script Writers and Aspiring Software Architects",
        "Focus: Code Readability and Maintainability"
    ]),
    ("IN SCOPE: Guard Clauses", [
        "Definition: Preventing Deep Nesting",
        "Early Exit from Functions or Loops",
        "Resources: Codementor Article, Wikipedia"
    ]),
    ("IN SCOPE: Single-Pass Loops", [
        "Single-Pass Loops Emulate Try-Catch",
        "Benefits: Clarity and Maintainability",
        "FileMaker Single-Pass Loop Example"
    ]),
    ("IF vs GUARD", [
        "Traditional IF Statements",
        "GUARD Clauses for Early Exits",
        "DEMO1: Enhanced Order Validation Example"
    ]),
    ("Choosing the Right Exit Strategy: 'Exit Loop If' within Single-Pass Loops", [
        "Single-Pass Loop Strategy Explained",
        "DEMO2: Scripted Example for 'Exit Loop If'",
        "Exit Script in the 'finally' Section"
    ]),
    ("Balancing Simplicity and Robustness in Control Flow", [
        "Best Practices in Control Flow",
        "Pros and Cons of 'Exit Loop If' Strategy",
        "Visual Aids: Flowchart, Code Snippet"
    ])
]

# Generate slides
for title, content in slides_content:
    slide_layout = prs.slide_layouts[1]  # 0 for title slide, 1 for title and content
    slide = prs.slides.add_slide(slide_layout)
    title_placeholder = slide.shapes.title
    content_placeholder = slide.placeholders[1]

    title_placeholder.text = title
    
    for line in content:
        p = content_placeholder.text_frame.add_paragraph()
        p.text = line
        p.level = 0

# Save presentation
prs.save('coding_practices_presentation.pptx')

print("Presentation has been generated.")

# Open slides
os.system("open coding_practices_presentation.pptx")