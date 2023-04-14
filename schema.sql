CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL
);

CREATE TABLE sprints (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    effort_estimated INTEGER NOT NULL,
    cost_estimated NUMERIC(10,2) NOT NULL,
    project_id INTEGER REFERENCES projects(id)
);
