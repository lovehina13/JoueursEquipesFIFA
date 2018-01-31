# coding: utf-8

#===============================================================================
# Name        : JoueursEquipesFIFA.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (03/10/2017)
# Description : Récupération des joueurs et des équipes FIFA
#===============================================================================

class Joueur(object):

    def __init__(self, nom, poste, note):
        self.nom = nom
        self.poste = poste
        self.note = note

def recupererPageJoueur(adresseHTTP):
    from urllib2 import Request, urlopen
    requete = Request(adresseHTTP, headers={"User-Agent": "Magic Browser"})
    texteHTML = "".join(urlopen(requete).readlines())
    texteHTML = texteHTML.replace("Math.round(a)", "a")
    texteHTML = texteHTML.replace("html(a)", "html(Math.round(a*1000)/1000)")
    return texteHTML

def recupererEquipes(joueurs, formation):
    equipes = []
    for joueur_1 in [joueur for joueur in joueurs if joueur.poste == formation[0]]:
        for joueur_2 in [joueur for joueur in joueurs if joueur.poste == formation[1]]:
            for joueur_3 in [joueur for joueur in joueurs if joueur.poste == formation[2]]:
                for joueur_4 in [joueur for joueur in joueurs if joueur.poste == formation[3]]:
                    for joueur_5 in [joueur for joueur in joueurs if joueur.poste == formation[4]]:
                        for joueur_6 in [joueur for joueur in joueurs if joueur.poste == formation[5]]:
                            for joueur_7 in [joueur for joueur in joueurs if joueur.poste == formation[6]]:
                                for joueur_8 in [joueur for joueur in joueurs if joueur.poste == formation[7]]:
                                    for joueur_9 in [joueur for joueur in joueurs if joueur.poste == formation[8]]:
                                        for joueur_10 in [joueur for joueur in joueurs if joueur.poste == formation[9]]:
                                            for joueur_11 in [joueur for joueur in joueurs if joueur.poste == formation[10]]:
                                                equipe = [joueur_1, joueur_2, joueur_3, joueur_4, joueur_5, joueur_6, joueur_7, joueur_8, joueur_9, joueur_10, joueur_11]
                                                equipeExclusive = reduce(lambda l, x: l if x in l else l + [x], equipe, [])
                                                if equipe == equipeExclusive:
                                                    equipes.append(equipe)
    return equipes

def recupererMeilleureEquipe(equipes):
    meilleureEquipe = None
    meilleureNoteEquipe = None
    for equipe in equipes:
        noteEquipe = 0.0
        for joueur in equipe:
            noteEquipe += joueur.note
        if noteEquipe > meilleureNoteEquipe or meilleureNoteEquipe is None:
            meilleureEquipe = equipe
            meilleureNoteEquipe = noteEquipe
    return meilleureEquipe

if __name__ == "__main__":
    # Récupération des joueurs
    version = 158865
    joueurs = [20801]
    for joueur in joueurs:
        adresseHTTP = "https://sofifa.com/player/calculator/" + str(joueur) + "?hl=fr-FR&v=18&e=" + str(version) + "&set=true"
        fichierHTML = "%d_%d.html" % (joueur, version)
        texteHTML = recupererPageJoueur(adresseHTTP)
        instanceFichier = open(fichierHTML, "w")
        instanceFichier.write(texteHTML)
        instanceFichier.close()
    # Récupération de l'équipe
    joueurs = [Joueur("Gardien", "G", 80.0),
               Joueur("Défenseur_droit", "DD", 80.0),
               Joueur("Défenseur_central_1", "DC", 80.0),
               Joueur("Défenseur_central_2", "DC", 80.0),
               Joueur("Défenseur_gauche", "DG", 80.0),
               Joueur("Milieu_droit", "MD", 80.0),
               Joueur("Milieu_central_1", "MC", 80.0),
               Joueur("Milieu_central_2", "MC", 80.0),
               Joueur("Milieu_gauche", "MG", 80.0),
               Joueur("Buteur_1", "BU", 80.0),
               Joueur("Buteur_2", "BU", 80.0)]
    formation = ["G", "DD", "DC", "DC", "DG", "MD", "MC", "MC", "MG", "BU", "BU"]
    equipes = recupererEquipes(joueurs, formation)
    meilleureEquipe = recupererMeilleureEquipe(equipes)
    if meilleureEquipe is not None:
        for index in range(len(formation)):
            poste = formation[index]
            joueur = meilleureEquipe[index]
            print "%s\t%s (%.3f)" % (poste, joueur.nom, joueur.note)
