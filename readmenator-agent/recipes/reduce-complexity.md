# Recipe: Reduce File Complexity

Target hotspot: `willmore_crsital2.py`
(complexity 1.0, centrality 0.8)

1. Read dependents: `grep -n 'willmore_crsital2.py' readmenator-agent/ARCHITECTURE.md`
2. Extract functions/classes into new files in the same subsystem
3. Update imports
4. Regenerate: `readmenator .`
