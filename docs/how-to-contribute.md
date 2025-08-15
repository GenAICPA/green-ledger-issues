---
sidebar_position: 2
title: How to Contribute
---

# How to Contribute (Even if You Think Git is a Type of British Insult)

Welcome! We're thrilled you're here to help us shape the future of sustainability accounting. This project is for everyone, especially sustainability specialists, accountants, and anyone passionate about a greener future. You don't need to be a coding wizard to contribute.

## The Easiest Way to Contribute: The GitHub Web Interface

Forget the command line, cryptic commands, and all that technical jargon. You can contribute directly from your web browser. Here's how:

### 1. Create a GitHub Account

If you don't have a GitHub account, you'll need to create one. It's free and only takes a minute. Think of it as your passport to the world of collaborative projects.

### 2. Find a Page You Want to Change

Navigate to the question or page you want to edit. As you're reading, you'll see an "Edit this page" link at the bottom. Click it!

![Edit this page link](/img/edit-this-page.png)  *<-- (We'll need to add an image here)*

### 3. Propose Your Change

Once you click the link, you'll be taken to the GitHub editor. It's just like a regular text editor. Make your changes directly in the browser.

When you're done, scroll to the bottom of the page. You'll see a box that says "Propose changes". Write a brief, friendly description of your change (e.g., "Added a clarification to Q5" or "Fixed a typo").

![Propose changes](/img/propose-changes.png) *<-- (We'll need to add an image here)*

Then, click the green "Propose changes" button.

### 4. What Happens Next? (The Magic of Pull Requests)

When you propose a change, you're creating what's called a "Pull Request." It's a fancy term for "a suggestion to change the official document." It doesn't mean your change is automatically accepted. It just means you're starting a conversation.

The project maintainers will be notified of your suggestion. They might ask you a few questions or suggest some changes. Once everyone is happy, your contribution will be merged into the main document, and you'll be an official contributor!

## Start a Discussion with an "Issue"

If you don't want to propose a change directly, but you have a question, an idea, or a comment, you can create an "Issue."

1.  Go to the [**Issues tab**](https://github.com/GenAICPA/green-ledger-issues/issues) of our GitHub repository.
2.  Click the "New issue" button.
3.  Choose one of the templates (e.g., "Question Discussion") and fill it out.

This is a great way to start a conversation with the community.

## Adding a New Question (A Live Example!)

Have a burning question that you think is missing from our list? We encourage you to add it! Here's how we just added Question 52, which deals with the "language gap" between accountants and engineers:

1.  **Create a New File:** In the `docs/questions` directory, we created a new file named `Q52.md`. The name is important: `Q` followed by the next number in the sequence.

2.  **Format the Question:** Inside the file, we added the question and a short and detailed answer. We also added a `sidebar_position` at the top of the file to make sure it appears in the right order.

3.  **Add it to the Sidebar:** To make the new question appear in the "All Questions" list on the website, we opened the `sidebars.js` file and added `'questions/Q52'` to the `items` array under the "All Questions" category.

That's it! If you're not comfortable with these steps, don't worry. You can always start a discussion with an "Issue" and propose your new question there. We're happy to help.

We're excited to have you on board. Let's build the Green Ledger together!
