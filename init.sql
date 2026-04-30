-- Utilisateurs (mot de passe = "password123" pour tous)
INSERT INTO users (name, email, password, role) VALUES
('Amina Kernou', 'amina@mail.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtG7Z8H3ZKGFuTjkP5RJm6QqGSuu', 'admin'),
('Samy Tamazirt', 'samy@mail.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtG7Z8H3ZKGFuTjkP5RJm6QqGSuu', 'membre'),
('Asala Nasri', 'asala@mail.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtG7Z8H3ZKGFuTjkP5RJm6QqGSuu', 'membre');

-- Profils
INSERT INTO profiles (bio, phone, adresse, avatar, user_id) VALUES
('Passionnée de lecture', '0612345678', 'Paris 13', null, 1),
('Etudiant M1 Info', '0698765432', 'Paris 18', null, 2);

-- Categories
INSERT INTO categories (name) VALUES
('Technologie'),
('Science'),
('Culture');

-- Articles
INSERT INTO articles (title, content, date, auteur_id) VALUES
('Introduction à FastAPI', 'FastAPI est un framework moderne...', '2026-04-20', 1),
('Docker pour les débutants', 'Docker permet de conteneuriser...', '2026-04-20', 2);

-- Commentaires
INSERT INTO comments (body, date, article_id, user_id) VALUES
('Super article merci !', '2026-04-20', 1, 2),
('Très utile pour notre projet', '2026-04-22', 1, 3),
('Docker c est vraiment pratique', '2026-04-23', 2, 1);