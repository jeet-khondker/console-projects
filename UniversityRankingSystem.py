class University:

    def __init__(self, name, establishment_year, ranking):
        self.name = name
        self.establishment_year = establishment_year
        self.ranking = ranking

    def show_universityRanking(self):
        print(self.name + " is at " + self.ranking + " position of the global university ranking.")

    def find_establishmentYear(self):
        print(self.name + " was established in the year " + str(self.establishment_year))

diu = University("Daffodil International University", 2002, '4th')
ju = University("Jahangirnagar University", 1990, '3rd')
buet = University("Bangladesh University of Engineering and Technology", 1971, '1st')

diu.show_universityRanking()
diu.find_establishmentYear()

ju.show_universityRanking()
ju.find_establishmentYear()

buet.show_universityRanking()
buet.find_establishmentYear()