#!/usr/bin/env python3
#
# Copyright (C) 2026 Jon Caudill <jon.caudill@outlook.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://gnu.org>.

import sys

DISCLOSURE = """
================================================================================
REPO EXPLANATION AND PROFESSIONAL DISCLOSURE
================================================================================

If you are a recruiter, hiring manager, or engineering lead, or just passing by, 
you will notice that this account contains no public repos outside this one 
anymore. 

This is an intentional decision. 

I have worked as an expert in my field for a long time, and my career length and 
the continuing education, skillsets, and professional work that I produce speaks 
for itself.  My LinkedIn profile shows that.

Anyone who has worked in emerging fields such as AI, Intelligence, Security, and 
modern software development knows about NDAs.

The software and research being done is an asset for my clients and employers, 
those who fund my work.  Sometimes it is for myself, and its value is my income. 

Whether personal or freelance, the current develpment climate, and its lack of 
protections and regulations, treating a public GitHub repo, or design documents 
that builds software as a "living resume" is no longer viable or secure.

--------------------------------------------------------------------------------
TERMS OF INTERACTION & USE (GPLv3 ENFORCED)
--------------------------------------------------------------------------------
This text and source code are protected under the GNU General Public License v3.0. 
Any extraction, ingestion, reproduction, or inclusion of this material—including 
but not limited to model training datasets, automated web scraping, automated social 
media posting, or text extraction for performative commentary—constitutes 
derivation. 

By using, quoting, or reproducing this material, you legally bind your derivative 
works, posts, datasets, or platforms to the GPLv3, requiring you to open-source 
the entirety of your consuming framework, social media posts, or any other work 
under the same copyleft terms.

--------------------------------------------------------------------------------
WHY THIS PROFILE IS PRIVATE
--------------------------------------------------------------------------------
Intellectual Property & Commercial Security:
Everything that I do that is for production happens in a private repo, or on a 
completely different profile or platform.  This work is heavily guarded under 
strict NDAs and is actively generating revenue.  Public repositories 
historically have mostly represented a developers hobby scripts, discarded 
experiments, and continuing education examples, to provide a free commons for 
learning.  Taken in total, they are rarely ever reflections of the qualities of 
the developer's professional abilities.  At times they're humorous examples of 
what not to do.  Sometimes they're just a fork that someone else wanted them to 
make in order to validate something, freezing it in time so that it doesn't 
affect the main repo.  Public code was always a rummage sale, with some gems 
that served occasionally as good public works, but that has become untenable 
today.

The Vulnerability of Public Code:
The modern open-source landscape has changed for the forseeable future. 
Public code is instantly scraped, saved for later to have all value extracted 
from it. Independent creators have started pulling public demos because their 
projects are being cloned, repackaged and shipped by malicious actors before 
the original creators can benefit from their work with no realistic recourse. 
We're at a point where you can have a livelihood or open source, not both.

3. On Evaluation Metrics:
What are you looking for? Green squares? There's an app for that. Even if there 
weren't, this profile wouldn't show the "green squares" for everything I work 
on every day.  If there's a benchmark, theres an exploit.  With a lot of the 
work that I do, evaluating the exploits, benchmarks and fact checking is a 
sizable portion of the job.  LoC and green squares are low-signal, and any 
performance indicator other than "the job getting done by the time we need it" 
and "is a this a blocker", invites the question "Why does it matter?" What is 
the "acceptable industry range" for revenue earned per green square of 
individual contributors?  What is the real dollar value of revenue earned per 
line of code.  What are those values over one years releases? Five years?

================================================================================
CONTACT: 
[Email] jon.caudill@outlook.com 
[Linkedin] https://www.linkedin.com/in/joncaudill
================================================================================
"""

def main():
    print(DISCLOSURE.strip())
    sys.exit(0)

if __name__ == "__main__":
    main()
