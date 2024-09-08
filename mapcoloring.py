from ortools.sat.python import cp_model

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

#GOAL: Find an assignment of frequencies to antanne that maintains the constraint that no
#atannate share similar frequencies


## colors: 0: Red, 1: Blue 2: Green
frequencies = {0: "f1", 1: "f2", 2: "f3"}

colors = {0 : 'Red',1:'Blue',2:'Green'}


SF = model.NewIntVar(0,2,'SF')
Alameda = model.NewIntVar(0,2,'Alameda')
Marin = model.NewIntVar(0,2,'Marin')
SanMateo = model.NewIntVar(0,2,'San Mateo')
SantaClara = model.NewIntVar(0,2,'Santa Clara')
ContraCosta = model.NewIntVar(0,2,'Contra Costa')
Solano = model.NewIntVar(0,2,'Solano')
Napa = model.NewIntVar(0,2,'Napa')
Sonoma = model.NewIntVar(0,2,'Sonoma')

Antenna1 = model.NewIntVar(0,2, "A1")
Antenna2 = model.NewIntVar(0,2, "A2")
Antenna3 = model.NewIntVar(0,2, "A3")
Antenna4 = model.NewIntVar(0,2, "A4")
Antenna5 = model.NewIntVar(0,2, "A5")
Antenna6 = model.NewIntVar(0,2, "A6")
Antenna7 = model.NewIntVar(0,2, "A7")
Antenna8 = model.NewIntVar(0,2, "A8")
Antenna9 = model.NewIntVar(0,2, "A9")


model.Add(Antenna1 != Antenna2)
model.Add(Antenna1 != Antenna3)
model.Add(Antenna1 != Antenna4)

model.Add(Antenna2 != Antenna1)
model.Add(Antenna2 != Antenna3)
model.Add(Antenna2 != Antenna5)
model.Add(Antenna2 != Antenna6)

model.Add(Antenna3 != Antenna1)
model.Add(Antenna3 != Antenna2)
model.Add(Antenna3 != Antenna6)
model.Add(Antenna3 != Antenna9)

model.Add(Antenna4 != Antenna1)
model.Add(Antenna4 != Antenna2)
model.Add(Antenna4 != Antenna5)

model.Add(Antenna5 != Antenna2)
model.Add(Antenna5 != Antenna4)

model.Add(Antenna6 != Antenna2)
model.Add(Antenna6 != Antenna7)
model.Add(Antenna6 != Antenna8)

model.Add(Antenna7 != Antenna6)
model.Add(Antenna7 != Antenna8)

model.Add(Antenna8 != Antenna7)
model.Add(Antenna8 != Antenna9)

model.Add(Antenna9 != Antenna3)
model.Add(Antenna9 != Antenna8)



## add edges. These are constraints. The edges are added so they wont intersect with each other

model.Add(SF != Alameda)
model.Add(SF != Marin)
model.Add(SF != SanMateo)
model.Add(ContraCosta != Alameda)
model.Add(Alameda != SanMateo)
model.Add(Alameda != SantaClara)
model.Add(SantaClara != SanMateo)
model.Add(Marin != Sonoma)
model.Add(Sonoma != Napa)
model.Add(Napa != Solano)
model.Add(Solano != ContraCosta)
model.Add(ContraCosta != Marin)

status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("A1: %s" % frequencies[solver.Value(Antenna1)])
    print("A2: %s" % frequencies[solver.Value(Antenna2)])
    print("A3: %s" % frequencies[solver.Value(Antenna3)])
    print("A4: %s" % frequencies[solver.Value(Antenna4)])
    print("A5: %s" % frequencies[solver.Value(Antenna5)])
    print("A6: %s" % frequencies[solver.Value(Antenna6)])
    print("A7: %s" % frequencies[solver.Value(Antenna7)])
    print("A8: %s" % frequencies[solver.Value(Antenna8)])
    print("A9: %s" % frequencies[solver.Value(Antenna9)])



    print("SF: %s" % colors[solver.Value(SF)])
    print("Alameda: %s" % colors[solver.Value(Alameda)])
    print("Marin: %s" % colors[solver.Value(Marin)])
    print("Contra Costa: %s" % colors[solver.Value(ContraCosta)])
    print("Solano: %s" % colors[solver.Value(Solano)])
    print("Sonoma: %s" % colors[solver.Value(Sonoma)])
    print("Santa Clara: %s" % colors[solver.Value(SantaClara)])
    print("San Mateo: %s" % colors[solver.Value(SanMateo)])
    print("Napa: %s" % colors[solver.Value(Napa)])


