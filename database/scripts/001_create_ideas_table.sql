CREATE TABLE ideas (
  content text,
  author REFERENCES accounts
);
