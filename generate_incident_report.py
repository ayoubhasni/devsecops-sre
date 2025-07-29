from datetime import datetime

incident_time = datetime.now().strftime("%d %B %Y à %H:%M")

report = f"""
# Rapport d’incident - API TODO : Erreur 500 simulée

## Contexte
Le {incident_time}, dans le cadre du TD DevSecOps/SRE, une panne simulée a été déclenchée sur l’API TODO. Cette API est une application Flask gérant une liste de tâches. La simulation a consisté à appeler volontairement l’endpoint `/error` qui provoque une erreur interne (division par zéro).

## Détection et diagnostic
L’incident a été détecté via le monitoring Prometheus et Grafana, avec une montée rapide du taux d’erreurs HTTP 5xx sur l’API. Les logs de l’application Flask ont confirmé une exception `ZeroDivisionError` liée à l’endpoint `/error`. Cette détection a permis de valider l’efficacité du système de monitoring et des métriques exposées.

## Cause racine
La cause racine est un bug intentionnel dans le code source de l’API, au niveau de la route `/error` qui exécute une division par zéro pour simuler un crash. Ce comportement est prévu dans le cadre des tests d’incidents.

## Actions correctives et rétablissement
Aucune correction n’a été nécessaire puisque l’erreur était volontaire et contrôlée. Le service est resté globalement disponible pour les autres endpoints, et le monitoring a correctement remonté l’incident. L’appel à `/error` a permis de confirmer la bonne configuration du pipeline de détection.

## Leçons apprises et actions préventives
- Validation complète de la chaîne de monitoring (exposition des métriques, collecte par Prometheus, visualisation dans Grafana).
- Confirmation de la pertinence des métriques 5xx pour détecter rapidement les erreurs critiques.
- Importance d’ajouter des alertes automatiques sur ces métriques pour améliorer le temps de réaction.
- Recommandation future : étendre la simulation d’incidents pour inclure d’autres types d’erreurs et tester la résilience globale.

---

**Rédigé automatiquement par script**  
**Date :** {incident_time}
"""

with open("incident-report.md", "w", encoding="utf-8") as f:
    f.write(report)

print("Rapport d’incident généré dans incident-report.md")
