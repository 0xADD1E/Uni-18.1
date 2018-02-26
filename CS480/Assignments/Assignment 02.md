# Assignment 2
## User Stories
- User Management
    - DB
- Initial Frontend
- Search
    - Book storage schema
- UI Rework and beautification
- Wishlist
- Rating and Review System
- Purchase System (pre-built)
- Purchase System (in-house)
    - PCI Compliance
- Performance Tuning
## Estimates
Time to intial release: 42 days

Time for all USs currently defined: 98 days
## Iteration Planning
21 Day Iterations for first two, switching to 14 day iterations afterward

- Iteration 1: User management, basic site design
- Iteration 2: Search, and payment making heavy use of off-the-shelf technologies
- Iteration 3: Site design cleanups
- Iteration 4: Wishlist, Rating and Review system
- Iteration 5: In-House purchase system
- Iteration 6: Performance Tuning
## Big User Stories
User Management requires a lot of basic work to get databases and minimal scaffolding working. There are a lot of web frameworks (Django comes to mind) that help with this phase, but even so, it's a big step.

Search is a really big project, and you always need either Apache Solar, or some people with PhDs to come up with an efficient way of searching a large dataset.

PCI Compliance in general is something that will take an entire cycle in and of itself, but this can be done for the initial release with something such as square or stripe

All three of these can do fit into an iteration with the use of pre-built technologies, but the later releases will take several iterations.
## Assumptions
- Management is okay with us using a pre-built PCI system initially (not a continued risk, as we later go on to build our own)
- Hosting, deployment, and scaling is a non-issue (always and continuously risky, though this can be significantly minimized with cloud technologies, and smart infrastructure design)
- Folks are capable of continuously meeting deadlines (this is a class. please don't make me get into this)