def inicializar_stats(rounds):
    stats = {}
    for jugador in rounds[0]["scores"]:
        stats[jugador] = {"total":0, "rondas_ganadas":0, "mejor_ronda":0, "promedio":0}
    return stats

def rondas(rounds,stats):
    for i in range(len(rounds)):
        mejor_jugador = None
        mejor_puntaje = -1
        ronda = rounds[i]
        print(f"Ronda {i} - {ronda["theme"]}:")
        for jugador in ronda["scores"]:
            puntaje_jugador = sum(ronda["scores"][jugador].values())
            stats[jugador]["total"] += puntaje_jugador
            if puntaje_jugador > mejor_puntaje:
                mejor_jugador = jugador
                mejor_puntaje = puntaje_jugador
            if puntaje_jugador > stats[jugador]["mejor_ronda"]:
                stats[jugador]["mejor_ronda"] = puntaje_jugador
        stats[mejor_jugador]["rondas_ganadas"] += 1
        print(f"Ganador: {mejor_jugador} ({mejor_puntaje} pts)")
        print(f"{'Tabla de posiciones':>21}")
        tabla = sorted(stats.items(), key=lambda x:x[1]["total"], reverse=True)
        for jugador, datos in tabla:
            print(f"{'':>3} {jugador:<10}| {datos["total"]} pts total")
        print()
    for jugador in stats:
        stats[jugador]["promedio"] = stats[jugador]["total"] / len(rounds)
    return stats, tabla

def imprimir_tabla_final(tabla):
    print("Tabla de posiciones final:")
    print(f"{'Cocinero':<10} | {'Puntaje':<7} | {'Rondas ganadas':<10} | {'Mejor ronda':<10} | Promedio")
    print("---------------------------------------------------------------")
    for jugador, datos in tabla:
        print(f"{jugador:<10} | {datos['total']:^7} | {datos['rondas_ganadas']:^14} | {datos['mejor_ronda']:^11} | {datos['promedio']:^8}")
    print("---------------------------------------------------------------")