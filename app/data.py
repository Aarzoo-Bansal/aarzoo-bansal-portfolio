"""Static content for the portfolio site.

Keeping page/content data here (separate from the app factory and routes in
__init__.py) is a common practice: routes stay thin and focused on request
handling, while content is easy to find and edit in one place.
"""

# Pages shown in the dynamic navigation bar.
# Each entry maps a display name to its URL.
PAGES = [
    {"name": "Home", "url": "/"},
    {"name": "Experience", "url": "/experience"},
    {"name": "Education", "url": "/education"},
    {"name": "Hobbies", "url": "/hobbies"},
    {"name": "Map", "url": "/map"},
]

# Work experience, most recent first. Rendered by a Jinja loop in experience.html.
EXPERIENCES = [
    {
        "role": "Production Engineering Fellow",
        "company": "MLH Fellowship",
        "dates": "Jun 2026 – Present",
        "awards": [],
        "bullets": [
            "Selected for Major League Hacking's Production Engineering track, "
            "collaborating with a pod of fellows on real-world software projects.",
        ],
    },
    {
        "role": "Open Source Contributor",
        "company": "Open Source",
        "dates": "",
        "awards": [],
        "bullets": [
            "Fixed vue/require-name-property and vue/require-explicit-emits ESLint violations across 60 Vue components in 6 MRs to gitlab-org/gitlab; navigated full OSS contribution cycle including CI debugging and maintainer collaboration.",
        ],
    },
    {
        "role": "Software Engineer Intern",
        "company": "AllayAI",
        "dates": "Sep 2025 – Dec 2025",
        "awards": [],
        "bullets": [
            "Engineered a rich-text-preserving clipboard solution in Flutter for "
            "AI-generated clinical notes, enabling physicians to copy directly into "
            "Epic EHR, eliminating manual formatting and saving ~2-5 minutes per note "
            "for 20+ doctors.",
            "Deployed a note-filtering system with persistent storage using "
            "Flutter/Dart, BLoC state management, and MySQL, enabling physicians to "
            "customize and sync documentation views across devices, saving ~5 minutes "
            "of daily setup time.",
            "Performed end-to-end manual testing across staging and production, "
            "identifying and resolving platform-specific bugs including link failures "
            "on Android and note rendering issues on mobile, ensuring consistent "
            "cross-platform behavior across 3 platforms (web, Android, iOS) before "
            "physician-facing releases.",
        ],
    },
    {
        "role": "Teaching Assistant",
        "company": "Northeastern University",
        "dates": "Sep 2024 – Aug 2025",
        "awards": [],
        "bullets": [
            "CS5800 Algorithms — Conducted office hours, graded assignments, and "
            "guided 40+ graduate students through complex algorithm design and analysis.",
            "CS5520 Mobile App Development — Supported students building Android "
            "Native applications using Java and reviewed code submissions.",
            "CS5008 Data Structures & Algorithms in Computer Systems — Sole TA for "
            "20+ graduate students; held extra office hours to strengthen foundations "
            "across linked lists, trees, and graphs, adapting teaching approaches to "
            "individual learning styles.",
            "Built educational tools including a Jeopardy-style quiz platform for NU AIG.",
        ],
    },
    {
        "role": "Software Engineer II",
        "company": "KPMG Global Services",
        "dates": "Aug 2021 – May 2023",
        "awards": ["Encore Rising Star", "Encore Rockstar"],
        "bullets": [
            "Developed and integrated a badge-scan check-in REST API and system for "
            "1000+ employees using JavaScript and relational database queries, "
            "collaborating with hardware and facilities teams to define API contracts, "
            "implement validation logic, and document integration endpoints — resulting "
            "in reliable real-time attendance tracking and preventing false check-ins.",
            "Built an automated employee onboarding pipeline integrating with SAP "
            "SuccessFactors API for data ingestion, validation, transformation, and "
            "database persistence, ensuring seamless synchronization and replacing "
            "manual onboarding efforts.",
            "Debugged and optimized an asset classification pipeline integrating "
            "external REST APIs by analyzing application logs, tracing API call "
            "failures, and refining validation logic, reducing processing errors and "
            "manual rework by approximately 75%.",
            "Led Software Asset Management training for 150+ colleagues, achieving a "
            "41% certification success rate.",
        ],
    },
    {
        "role": "Software Engineer II",
        "company": "Infosys Limited",
        "dates": "Jul 2018 – Aug 2021",
        "awards": ["4× Insta Award Recipient"],
        "bullets": [
            "Programmed a customer-facing asset management platform for a telecom "
            "provider using Angular and JavaScript in an Agile environment, enabling "
            "320+ retail locations to process device trade-ins and manage warranty claims.",
            "Implemented multi-system API integrations — including lost/stolen device "
            "verification, Apple device diagnostics, and AWS S3 storage for device "
            "images — improving operational efficiency by 60% across trade-in, "
            "warranty, and repair workflows.",
            "Cut production errors by 80% by standardizing deployment checklists and "
            "validation steps on the go-live team.",
        ],
    },
    {
        "role": "Software Engineer Intern",
        "company": "Infosys Limited",
        "dates": "Feb 2018 – May 2018",
        "awards": [],
        "bullets": [
            "Developed a full-stack job portal using Java, Hibernate ORM, and "
            "responsive web design, implementing CRUD operations with role-based "
            "access — allowing job seekers to filter opportunities by skills and "
            "location, and employers to post jobs, discover candidates, and email "
            "them directly from the platform.",
        ],
    },
]

# Hobbies, shown as polaroid cards in hobbies.html.
# "image" is a filename inside app/static/img/.
HOBBIES = [
    {
        "name": "Travelling",
        "image": "travelling.png",
        "caption": "Chasing new cultures and views across three continents.",
    },
    {
        "name": "Painting",
        "image": "painting.png",
        "caption": "Unwinding with a canvas and a splash of color.",
    },
    {
        "name": "Cooking",
        "image": "cooking.png",
        "caption": "Experimenting with recipes from around the world.",
    },
    {
        "name": "Dancing",
        "image": "dancing1.png",
        "caption": "Moving to the rhythm whenever the music's on.",
    },
]

# Places I've visited, shown as pins on a Leaflet map in map.html.
# lat/lng are the map coordinates for each pin; note shows in the popup.
PLACES = [
    {"name": "Jaypee University of IT, Solan", "lat": 31.0254, "lng": 77.0664,
     "note": "B.Tech in Information Technology"},
    {"name": "Agra, India", "lat": 27.1767, "lng": 78.0081,
     "note": "Lived here for some years"},
    {"name": "Delhi, India", "lat": 28.6139, "lng": 77.2090,
     "note": "Got married here"},
    {"name": "San Francisco, USA", "lat": 37.7749, "lng": -122.4194,
     "note": "First place I visited in the US"},
    {"name": "San Jose, USA", "lat": 37.3382, "lng": -121.8863,
     "note": "Master's"},
    {"name": "Alaska, USA", "lat": 61.2181, "lng": -149.9003,
     "note": "Saw my first glacier"},
    {"name": "New York City, USA", "lat": 40.7128, "lng": -74.0060,
     "note": ""},
    {"name": "Glacier National Park, USA", "lat": 48.6968, "lng": -113.7183,
     "note": ""},
    {"name": "Idaho, USA", "lat": 43.6150, "lng": -116.2023,
     "note": ""},
    {"name": "Colorado, USA", "lat": 39.7392, "lng": -104.9903,
     "note": ""},
    {"name": "Kuala Lumpur, Malaysia", "lat": 3.1390, "lng": 101.6869,
     "note": ""},
    {"name": "Singapore", "lat": 1.3521, "lng": 103.8198,
     "note": ""},
    {"name": "Switzerland", "lat": 46.8182, "lng": 8.2275,
     "note": ""},
    {"name": "Germany", "lat": 51.1657, "lng": 10.4515,
     "note": ""},
    {"name": "France", "lat": 46.2276, "lng": 2.2137,
     "note": ""},
    {"name": "Sri Lanka", "lat": 7.8731, "lng": 80.7718,
     "note": ""},
    {"name": "Bathinda, India", "lat": 30.2110, "lng": 74.9455,
     "note": ""},
    {"name": "Mumbai, India", "lat": 19.0760, "lng": 72.8777,
     "note": ""},
    {"name": "Bangalore, India", "lat": 12.9716, "lng": 77.5946,
     "note": ""},
    {"name": "Mysore, India", "lat": 12.2958, "lng": 76.6394,
     "note": ""},
    {"name": "Pune, India", "lat": 18.5204, "lng": 73.8567,
     "note": ""},
]
