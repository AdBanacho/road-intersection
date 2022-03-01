import random
import logging
import configparser
import copy
import numpy as np
from tqdm import tqdm


##########################################################################################
# Adrian Banachowicz - Genetic Algorithm
##########################################################################################


class GeneticAlgorithm:

    def __init__(self, f_creating_single_individual, f_calculation_of_mutation, f_calculation_of_criterion):

        self.parents = []
        self.population = []
        self.new_population = []
        self.selected_players = []
        self.selected_players_values = []
        self.criterion_in_every_generation = []
        config = configparser.ConfigParser()
        config.read('properties.ini')
        self.mutation_chance = float(config['settings']['MutationChance'])
        self.relation_of_select = config['settings']['RelationOfSelect']
        self.optimization_problem = config['settings']['OptimizationProblem']
        self.size_of_generation = int(config['settings']['SizeOfGeneration'])
        self.size_of_population = int(config['settings']['SizeOfPopulation'])
        self.size_of_tournament = int(config['settings']['SizeOfTournament'])
        self.count_of_genotypes = int(config['settings']['CountOfGenotypes'])
        self.count_of_mutated_genotypes = int(config['settings']['CountOfMutatedGenotypes'])
        self.best_parent = f_creating_single_individual()[0]
        self.best_criterion_value = f_creating_single_individual()[1]
        self.f_creating_single_individual = f_creating_single_individual
        self.f_calculation_of_mutation = f_calculation_of_mutation
        self.f_calculation_of_criterion = f_calculation_of_criterion
        logHandler = logging.StreamHandler()
        logHandler.setFormatter(logging.Formatter('%(message)s'))
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logHandler)

    def random_first_population(self):
        for _ in tqdm(range(self.size_of_population)):
            self.population.append(self.f_creating_single_individual()[0])

    def mutation(self):
        for parent in self.parents:
            if self.mutation_chance > np.random.rand(1):
                for _ in range(self.count_of_mutated_genotypes):
                    parent[np.random.randint(0, self.count_of_genotypes)] = self.f_calculation_of_mutation()

    def size_of_crossing(self):
        border_1, border_2 = np.random.randint(1, self.count_of_genotypes, 2)
        while border_1 == border_2:
            border_2 = np.random.randint(1, self.count_of_genotypes)
        return np.minimum(border_1, border_2), np.maximum(border_1, border_2)

    def crossing(self):
        b_1, b_2 = self.size_of_crossing()
        self.parents[0][b_1:b_2], self.parents[1][b_1:b_2] = \
            self.parents[1][b_1:b_2], self.parents[0][b_1:b_2]

    def select_the_players(self, population):
        self.selected_players.clear()
        no_of_selected_players = random.sample(range(len(population)), self.size_of_tournament)
        for p in no_of_selected_players:
            self.selected_players.append(population[p])

    def players_values_of_criterion(self):
        self.selected_players_values.clear()
        for player in self.selected_players:
            self.selected_players_values.append(self.f_calculation_of_criterion(player))

    def sort_players(self):
        self.players_values_of_criterion()
        self.selected_players_values, self.selected_players = \
            zip(*sorted(zip(self.selected_players_values, self.selected_players)))
        self.selected_players = list(self.selected_players)
        self.selected_players_values = list(self.selected_players_values)

    def tournament(self):
        self.parents.clear()
        self.sort_players()
        if self.relation_of_select == "MIN-MIN":
            self.parents.extend([self.selected_players[0], self.selected_players[1]])
        elif self.relation_of_select == "MIN-MAX":
            self.parents.extend([self.selected_players[0], self.selected_players[-1]])
        elif self.relation_of_select == "MAX-MAX":
            self.parents.extend([self.selected_players[-1], self.selected_players[-2]])

    def save_best_combination(self):
        for parent in self.parents:
            parent_criterion_value = self.f_calculation_of_criterion(parent)
            if self.optimization_problem == "MIN":
                if parent_criterion_value < self.best_criterion_value:
                    self.best_parent = parent
                    self.best_criterion_value = parent_criterion_value

            elif self.optimization_problem == "MAX":
                if parent_criterion_value > self.best_criterion_value:
                    self.best_parent = parent
                    self.best_criterion_value = parent_criterion_value

    def genetic_process(self):
        self.new_population.clear()
        for _ in range(self.size_of_population // 2):
            self.select_the_players(self.population)
            self.tournament()
            self.save_best_combination()
            self.crossing()
            self.save_best_combination()
            self.mutation()
            self.save_best_combination()
            self.new_population.extend(list(self.parents))

        self.population.extend(self.new_population)

    def select_new_population(self):
        self.new_population.clear()
        for _ in range(self.size_of_population // 2):
            self.select_the_players(self.population)
            self.tournament()
            self.new_population.extend(list(self.parents))
        self.population = copy.deepcopy(self.new_population)

    def run(self):
        self.logger.warning('Creating first population')
        self.random_first_population()
        self.logger.warning('Genetic process')
        for _ in tqdm(range(self.size_of_generation)):
            self.genetic_process()
            self.select_new_population()
            self.criterion_in_every_generation.append(self.best_criterion_value)


##########################################################################################
