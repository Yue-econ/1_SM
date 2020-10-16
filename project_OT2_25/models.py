import math
import random
from ast import literal_eval

from django.db import models


from decimal import *

from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, widgets)



#from otree_tools.models.fields import MultipleChoiceModelField


class Constants (BaseConstants):
    name_in_url = 'project_OT2_25'
    players_per_group = None
    players_per_round = 25
    patients_per_round = 24
    num_rounds = 30
    instructions_template = 'project_OT2_25/instruction.html'
    endowment_patient = 653
    painThreshold_increment = 0.01
    painThreshold_choices = [x/100 for x in range(0, 400)]
    per_visit_fee = c(103)
    price = c(15)
    price2 = c(550)
    weight_factor_health = 1.1
    id_in_group = (1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
    id_in_group_patient = (1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
    k_i = (0.94, 0.94, 0.94,0.94, 0.94, 0.94, 0.94,0.94,1.40, 1.40, 1.40,1.40,1.7, 1.7,1.7,1.7, 2.5, 2.5,2.5,2.5, 2.5, 2.5, 2.5, 2.5)
    r_i = (1000, 1000, 1000, 1000,1000, 1000,1000, 1000,165, 165, 165, 165, 50, 50, 50, 50, 250, 250, 250, 250, 250, 250, 250, 250)
    id_pain_dic = {id_in_group_patient: k_i}
    id_taste_dic = {id_in_group_patient: r_i}
    showupfee = 10
    segement1 = 0.94
    segement2 = 1.4
    segement3 = 1.7
    segement4 = 2.5


class Subsession (BaseSubsession):
    def creating_session(self):
        self.group_randomly (fixed_id_in_group=False)
        p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25 = self.get_players()
        physicians=[]
        if self.round_number == 5:
            for p in self.get_players():
                p1.id_in_group = 24
                p2.id_in_group = 1
                p3.id_in_group = 10
                p4.id_in_group = 3
                p5.id_in_group = 17
                p6.id_in_group = 4
                p7.id_in_group = 23
                p8.id_in_group = 2
                p9.id_in_group = 9
                p10.id_in_group = 6
                p11.id_in_group = 12
                p12.id_in_group = 7
                p13.id_in_group = 18
                p14.id_in_group = 8
                p15.id_in_group = 16
                p16.id_in_group = 11
                p17.id_in_group = 22
                p18.id_in_group = 20
                p19.id_in_group = 21
                p20.id_in_group = 19
                p21.id_in_group = 14
                p22.id_in_group = 5
                p23.id_in_group = 25
                p24.id_in_group = 15
                p25.id_in_group = 13

        if self.round_number == 6:
            for p in self.get_players():
                p1.id_in_group = 23
                p2.id_in_group = 2
                p3.id_in_group = 16
                p4.id_in_group = 10
                p5.id_in_group = 19
                p6.id_in_group = 9
                p7.id_in_group = 15
                p8.id_in_group = 14
                p9.id_in_group = 17
                p10.id_in_group = 22
                p11.id_in_group = 7
                p12.id_in_group = 12
                p13.id_in_group = 20
                p14.id_in_group = 13
                p15.id_in_group = 18
                p16.id_in_group = 6
                p17.id_in_group = 21
                p18.id_in_group = 3
                p19.id_in_group = 25
                p20.id_in_group = 4
                p21.id_in_group = 24
                p22.id_in_group = 8
                p23.id_in_group = 5
                p24.id_in_group = 1
                p25.id_in_group = 11

        if self.round_number == 7:
            for p in self.get_players():
                p1.id_in_group = 9
                p2.id_in_group = 25
                p3.id_in_group = 22
                p4.id_in_group = 12
                p5.id_in_group = 17
                p6.id_in_group = 16
                p7.id_in_group = 1
                p8.id_in_group = 10
                p9.id_in_group = 14
                p10.id_in_group = 21
                p11.id_in_group = 7
                p12.id_in_group = 23
                p13.id_in_group = 15
                p14.id_in_group = 11
                p15.id_in_group = 13
                p16.id_in_group = 4
                p17.id_in_group = 18
                p18.id_in_group = 3
                p19.id_in_group = 6
                p20.id_in_group = 24
                p21.id_in_group = 2
                p22.id_in_group = 19
                p23.id_in_group = 8
                p24.id_in_group = 20
                p25.id_in_group = 5

        if self.round_number == 8:
            for p in self.get_players():
                p1.id_in_group = 14
                p2.id_in_group = 8
                p3.id_in_group = 13
                p4.id_in_group = 16
                p5.id_in_group = 19
                p6.id_in_group = 15
                p7.id_in_group = 5
                p8.id_in_group = 12
                p9.id_in_group = 25
                p10.id_in_group = 10
                p11.id_in_group = 17
                p12.id_in_group = 4
                p13.id_in_group = 23
                p14.id_in_group = 21
                p15.id_in_group = 3
                p16.id_in_group = 2
                p17.id_in_group = 22
                p18.id_in_group = 11
                p19.id_in_group = 1
                p20.id_in_group = 18
                p21.id_in_group = 9
                p22.id_in_group = 24
                p23.id_in_group = 6
                p24.id_in_group = 20
                p25.id_in_group = 7

        if self.round_number == 9:
            for p in self.get_players():
                p1.id_in_group = 16
                p2.id_in_group = 11
                p3.id_in_group = 24
                p4.id_in_group = 15
                p5.id_in_group = 17
                p6.id_in_group = 12
                p7.id_in_group = 18
                p8.id_in_group = 21
                p9.id_in_group = 4
                p10.id_in_group = 25
                p11.id_in_group = 13
                p12.id_in_group = 22
                p13.id_in_group = 14
                p14.id_in_group = 3
                p15.id_in_group = 19
                p16.id_in_group = 10
                p17.id_in_group = 8
                p18.id_in_group = 23
                p19.id_in_group = 20
                p20.id_in_group = 5
                p21.id_in_group = 6
                p22.id_in_group = 7
                p23.id_in_group = 2
                p24.id_in_group = 1
                p25.id_in_group = 9

        if self.round_number == 10:
            for p in self.get_players():
                p1.id_in_group = 19
                p2.id_in_group = 2
                p3.id_in_group = 12
                p4.id_in_group = 5
                p5.id_in_group = 13
                p6.id_in_group = 11
                p7.id_in_group = 17
                p8.id_in_group = 16
                p9.id_in_group = 21
                p10.id_in_group = 15
                p11.id_in_group = 3
                p12.id_in_group = 22
                p13.id_in_group = 23
                p14.id_in_group = 7
                p15.id_in_group = 1
                p16.id_in_group = 8
                p17.id_in_group = 6
                p18.id_in_group = 25
                p19.id_in_group = 14
                p20.id_in_group = 20
                p21.id_in_group = 10
                p22.id_in_group = 9
                p23.id_in_group = 24
                p24.id_in_group = 4
                p25.id_in_group = 18

        if self.round_number == 11:
            for p in self.get_players():
                p1.id_in_group = 15
                p2.id_in_group = 8
                p3.id_in_group = 24
                p4.id_in_group = 25
                p5.id_in_group = 12
                p6.id_in_group = 7
                p7.id_in_group = 13
                p8.id_in_group = 21
                p9.id_in_group = 23
                p10.id_in_group = 1
                p11.id_in_group = 11
                p12.id_in_group = 10
                p13.id_in_group = 17
                p14.id_in_group = 19
                p15.id_in_group = 4
                p16.id_in_group = 20
                p17.id_in_group = 18
                p18.id_in_group = 5
                p19.id_in_group = 16
                p20.id_in_group = 6
                p21.id_in_group = 14
                p22.id_in_group = 22
                p23.id_in_group = 9
                p24.id_in_group = 2
                p25.id_in_group = 3
        if self.round_number == 12:
            for p in self.get_players():
                p1.id_in_group = 25
                p2.id_in_group = 19
                p3.id_in_group = 13
                p4.id_in_group = 22
                p5.id_in_group = 2
                p6.id_in_group = 6
                p7.id_in_group = 5
                p8.id_in_group = 18
                p9.id_in_group = 9
                p10.id_in_group = 3
                p11.id_in_group = 4
                p12.id_in_group = 23
                p13.id_in_group = 15
                p14.id_in_group = 20
                p15.id_in_group = 7
                p16.id_in_group = 10
                p17.id_in_group = 16
                p18.id_in_group = 11
                p19.id_in_group = 12
                p20.id_in_group = 8
                p21.id_in_group = 14
                p22.id_in_group = 17
                p23.id_in_group = 21
                p24.id_in_group = 24
                p25.id_in_group = 1

        if self.round_number == 13:
            for p in self.get_players():
                p1.id_in_group = 4
                p2.id_in_group = 24
                p3.id_in_group = 19
                p4.id_in_group = 21
                p5.id_in_group = 12
                p6.id_in_group = 11
                p7.id_in_group = 15
                p8.id_in_group = 7
                p9.id_in_group = 8
                p10.id_in_group = 20
                p11.id_in_group = 13
                p12.id_in_group = 16
                p13.id_in_group = 2
                p14.id_in_group = 18
                p15.id_in_group = 9
                p16.id_in_group = 5
                p17.id_in_group = 25
                p18.id_in_group = 14
                p19.id_in_group = 6
                p20.id_in_group = 3
                p21.id_in_group = 17
                p22.id_in_group = 1
                p23.id_in_group = 10
                p24.id_in_group = 23
                p25.id_in_group = 22

        if self.round_number == 14:
            for p in self.get_players():
                p1.id_in_group = 10
                p2.id_in_group = 8
                p3.id_in_group = 2
                p4.id_in_group = 6
                p5.id_in_group = 25
                p6.id_in_group = 20
                p7.id_in_group = 9
                p8.id_in_group = 4
                p9.id_in_group = 3
                p10.id_in_group = 12
                p11.id_in_group = 5
                p12.id_in_group = 17
                p13.id_in_group = 7
                p14.id_in_group = 23
                p15.id_in_group = 24
                p16.id_in_group = 14
                p17.id_in_group = 15
                p18.id_in_group = 22
                p19.id_in_group = 1
                p20.id_in_group = 16
                p21.id_in_group = 11
                p22.id_in_group = 18
                p23.id_in_group = 19
                p24.id_in_group = 13
                p25.id_in_group = 21

        if self.round_number == 15:
            for p in self.get_players():
                p1.id_in_group = 17
                p2.id_in_group = 12
                p3.id_in_group = 2
                p4.id_in_group = 1
                p5.id_in_group = 10
                p6.id_in_group = 20
                p7.id_in_group = 3
                p8.id_in_group = 25
                p9.id_in_group = 24
                p10.id_in_group = 11
                p11.id_in_group = 5
                p12.id_in_group = 15
                p13.id_in_group = 16
                p14.id_in_group = 23
                p15.id_in_group = 19
                p16.id_in_group = 13
                p17.id_in_group = 21
                p18.id_in_group = 18
                p19.id_in_group = 22
                p20.id_in_group = 7
                p21.id_in_group = 6
                p22.id_in_group = 4
                p23.id_in_group = 9
                p24.id_in_group = 14
                p25.id_in_group = 8

        if self.round_number == 16:
            for p in self.get_players():
                p1.id_in_group = 15
                p2.id_in_group = 3
                p3.id_in_group = 1
                p4.id_in_group = 20
                p5.id_in_group = 14
                p6.id_in_group = 18
                p7.id_in_group = 6
                p8.id_in_group = 21
                p9.id_in_group = 24
                p10.id_in_group = 9
                p11.id_in_group = 19
                p12.id_in_group = 7
                p13.id_in_group = 8
                p14.id_in_group = 17
                p15.id_in_group = 25
                p16.id_in_group = 10
                p17.id_in_group = 23
                p18.id_in_group = 4
                p19.id_in_group = 5
                p20.id_in_group = 22
                p21.id_in_group = 13
                p22.id_in_group = 11
                p23.id_in_group = 12
                p24.id_in_group = 2
                p25.id_in_group = 16

        if self.round_number == 17:
            for p in self.get_players():
                p1.id_in_group = 17
                p2.id_in_group = 18
                p3.id_in_group = 9
                p4.id_in_group = 24
                p5.id_in_group = 11
                p6.id_in_group = 10
                p7.id_in_group = 12
                p8.id_in_group = 2
                p9.id_in_group = 8
                p10.id_in_group = 6
                p11.id_in_group = 20
                p12.id_in_group = 16
                p13.id_in_group = 25
                p14.id_in_group = 1
                p15.id_in_group = 22
                p16.id_in_group = 5
                p17.id_in_group = 23
                p18.id_in_group = 19
                p19.id_in_group = 14
                p20.id_in_group = 13
                p21.id_in_group = 4
                p22.id_in_group = 21
                p23.id_in_group = 3
                p24.id_in_group = 15
                p25.id_in_group = 7

        if self.round_number == 18:
            for p in self.get_players():
                p1.id_in_group = 10
                p2.id_in_group = 7
                p3.id_in_group = 25
                p4.id_in_group = 2
                p5.id_in_group = 20
                p6.id_in_group = 15
                p7.id_in_group = 18
                p8.id_in_group = 12
                p9.id_in_group = 1
                p10.id_in_group = 13
                p11.id_in_group = 14
                p12.id_in_group = 5
                p13.id_in_group = 16
                p14.id_in_group = 23
                p15.id_in_group = 24
                p16.id_in_group = 3
                p17.id_in_group = 22
                p18.id_in_group = 4
                p19.id_in_group = 11
                p20.id_in_group = 17
                p21.id_in_group = 21
                p22.id_in_group = 8
                p23.id_in_group = 19
                p24.id_in_group = 9
                p25.id_in_group = 6

        if self.round_number == 19:
            for p in self.get_players():
                p1.id_in_group = 11
                p2.id_in_group = 3
                p3.id_in_group = 2
                p4.id_in_group = 13
                p5.id_in_group = 8
                p6.id_in_group = 14
                p7.id_in_group = 4
                p8.id_in_group = 12
                p9.id_in_group = 20
                p10.id_in_group = 18
                p11.id_in_group = 15
                p12.id_in_group = 17
                p13.id_in_group = 19
                p14.id_in_group = 16
                p15.id_in_group = 5
                p16.id_in_group = 7
                p17.id_in_group = 21
                p18.id_in_group = 9
                p19.id_in_group = 22
                p20.id_in_group = 10
                p21.id_in_group = 23
                p22.id_in_group = 6
                p23.id_in_group = 1
                p24.id_in_group = 24
                p25.id_in_group = 25

        if self.round_number == 20:
            for p in self.get_players():
                p1.id_in_group = 18
                p2.id_in_group = 11
                p3.id_in_group = 5
                p4.id_in_group = 1
                p5.id_in_group = 21
                p6.id_in_group = 25
                p7.id_in_group = 20
                p8.id_in_group = 7
                p9.id_in_group = 10
                p10.id_in_group = 9
                p11.id_in_group = 17
                p12.id_in_group = 2
                p13.id_in_group = 14
                p14.id_in_group = 8
                p15.id_in_group = 19
                p16.id_in_group = 23
                p17.id_in_group = 13
                p18.id_in_group = 6
                p19.id_in_group = 24
                p20.id_in_group = 15
                p21.id_in_group = 22
                p22.id_in_group = 3
                p23.id_in_group = 4
                p24.id_in_group = 12
                p25.id_in_group = 16

        if self.round_number == 21:
            for p in self.get_players():
                p1.id_in_group = 20
                p2.id_in_group = 16
                p3.id_in_group = 2
                p4.id_in_group = 1
                p5.id_in_group = 19
                p6.id_in_group = 12
                p7.id_in_group = 7
                p8.id_in_group = 18
                p9.id_in_group = 11
                p10.id_in_group = 5
                p11.id_in_group = 9
                p12.id_in_group = 8
                p13.id_in_group = 3
                p14.id_in_group = 23
                p15.id_in_group = 22
                p16.id_in_group = 14
                p17.id_in_group = 21
                p18.id_in_group = 4
                p19.id_in_group = 15
                p20.id_in_group = 13
                p21.id_in_group = 10
                p22.id_in_group = 6
                p23.id_in_group = 24
                p24.id_in_group = 25
                p25.id_in_group = 17

        if self.round_number == 22:
            for p in self.get_players():
                p1.id_in_group = 6
                p2.id_in_group = 5
                p3.id_in_group = 23
                p4.id_in_group = 19
                p5.id_in_group = 3
                p6.id_in_group = 4
                p7.id_in_group = 21
                p8.id_in_group = 16
                p9.id_in_group = 13
                p10.id_in_group = 10
                p11.id_in_group = 9
                p12.id_in_group = 12
                p13.id_in_group = 20
                p14.id_in_group = 17
                p15.id_in_group = 22
                p16.id_in_group = 25
                p17.id_in_group = 14
                p18.id_in_group = 1
                p19.id_in_group = 7
                p20.id_in_group = 11
                p21.id_in_group = 8
                p22.id_in_group = 2
                p23.id_in_group = 15
                p24.id_in_group = 18
                p25.id_in_group = 24

        if self.round_number == 23:
            for p in self.get_players():
                p1.id_in_group = 11
                p2.id_in_group = 18
                p3.id_in_group = 8
                p4.id_in_group = 6
                p5.id_in_group = 13
                p6.id_in_group = 20
                p7.id_in_group = 2
                p8.id_in_group = 10
                p9.id_in_group = 17
                p10.id_in_group = 24
                p11.id_in_group = 12
                p12.id_in_group = 3
                p13.id_in_group = 22
                p14.id_in_group = 7
                p15.id_in_group = 4
                p16.id_in_group = 15
                p17.id_in_group = 16
                p18.id_in_group = 19
                p19.id_in_group = 21
                p20.id_in_group = 25
                p21.id_in_group = 9
                p22.id_in_group = 5
                p23.id_in_group = 14
                p24.id_in_group = 23
                p25.id_in_group = 1

        if self.round_number == 24:
            for p in self.get_players():
                p1.id_in_group = 1
                p2.id_in_group = 4
                p3.id_in_group = 9
                p4.id_in_group = 12
                p5.id_in_group = 11
                p6.id_in_group = 2
                p7.id_in_group = 10
                p8.id_in_group = 21
                p9.id_in_group = 15
                p10.id_in_group = 8
                p11.id_in_group = 25
                p12.id_in_group = 13
                p13.id_in_group = 24
                p14.id_in_group = 20
                p15.id_in_group = 5
                p16.id_in_group = 17
                p17.id_in_group = 22
                p18.id_in_group = 19
                p19.id_in_group = 14
                p20.id_in_group = 3
                p21.id_in_group = 23
                p22.id_in_group = 7
                p23.id_in_group = 16
                p24.id_in_group = 18
                p25.id_in_group = 6

        if self.round_number == 25:
            for p in self.get_players():
                p1.id_in_group = 12
                p2.id_in_group = 14
                p3.id_in_group = 4
                p4.id_in_group = 13
                p5.id_in_group = 9
                p6.id_in_group = 15
                p7.id_in_group = 25
                p8.id_in_group = 7
                p9.id_in_group = 23
                p10.id_in_group = 11
                p11.id_in_group = 10
                p12.id_in_group = 17
                p13.id_in_group = 18
                p14.id_in_group = 24
                p15.id_in_group = 21
                p16.id_in_group = 20
                p17.id_in_group = 5
                p18.id_in_group = 2
                p19.id_in_group = 16
                p20.id_in_group = 8
                p21.id_in_group = 22
                p22.id_in_group = 3
                p23.id_in_group = 19
                p24.id_in_group = 6
                p25.id_in_group = 1
        if self.round_number == 26:
            for p in self.get_players():
                p1.id_in_group = 7
                p2.id_in_group = 15
                p3.id_in_group = 1
                p4.id_in_group = 16
                p5.id_in_group = 10
                p6.id_in_group = 2
                p7.id_in_group = 13
                p8.id_in_group = 20
                p9.id_in_group = 5
                p10.id_in_group = 8
                p11.id_in_group = 21
                p12.id_in_group = 25
                p13.id_in_group = 3
                p14.id_in_group = 24
                p15.id_in_group = 18
                p16.id_in_group = 14
                p17.id_in_group = 23
                p18.id_in_group = 19
                p19.id_in_group = 9
                p20.id_in_group = 17
                p21.id_in_group = 6
                p22.id_in_group = 22
                p23.id_in_group = 4
                p24.id_in_group = 11
                p25.id_in_group = 12

        if self.round_number == 27:
            for p in self.get_players():
                p1.id_in_group = 13
                p2.id_in_group = 19
                p3.id_in_group = 20
                p4.id_in_group = 4
                p5.id_in_group = 1
                p6.id_in_group = 14
                p7.id_in_group = 12
                p8.id_in_group = 6
                p9.id_in_group = 8
                p10.id_in_group = 16
                p11.id_in_group = 11
                p12.id_in_group = 22
                p13.id_in_group = 7
                p14.id_in_group = 25
                p15.id_in_group = 2
                p16.id_in_group = 24
                p17.id_in_group = 21
                p18.id_in_group = 3
                p19.id_in_group = 9
                p20.id_in_group = 17
                p21.id_in_group = 10
                p22.id_in_group = 15
                p23.id_in_group = 23
                p24.id_in_group = 5
                p25.id_in_group = 18

        if self.round_number == 28:
            for p in self.get_players():
                p1.id_in_group = 22
                p2.id_in_group = 5
                p3.id_in_group = 12
                p4.id_in_group = 9
                p5.id_in_group = 24
                p6.id_in_group = 14
                p7.id_in_group = 20
                p8.id_in_group = 23
                p9.id_in_group = 16
                p10.id_in_group = 4
                p11.id_in_group = 17
                p12.id_in_group = 3
                p13.id_in_group = 11
                p14.id_in_group = 15
                p15.id_in_group = 7
                p16.id_in_group = 10
                p17.id_in_group = 13
                p18.id_in_group = 8
                p19.id_in_group = 2
                p20.id_in_group = 21
                p21.id_in_group = 25
                p22.id_in_group = 6
                p23.id_in_group = 19
                p24.id_in_group = 18
                p25.id_in_group = 1

        if self.round_number == 29:
            for p in self.get_players():
                p1.id_in_group = 12
                p2.id_in_group = 7
                p3.id_in_group = 14
                p4.id_in_group = 8
                p5.id_in_group = 17
                p6.id_in_group = 19
                p7.id_in_group = 2
                p8.id_in_group = 4
                p9.id_in_group = 24
                p10.id_in_group = 13
                p11.id_in_group = 22
                p12.id_in_group = 6
                p13.id_in_group = 9
                p14.id_in_group = 18
                p15.id_in_group = 11
                p16.id_in_group = 23
                p17.id_in_group = 10
                p18.id_in_group = 3
                p19.id_in_group = 16
                p20.id_in_group = 20
                p21.id_in_group = 5
                p22.id_in_group = 25
                p23.id_in_group = 21
                p24.id_in_group = 1
                p25.id_in_group = 15

        #        if self.round_number == 1:
#            self.session.vars['not_yet_physician']=repr(list(range(1,26)))
#        self.group_randomly ()
#        not_yet_physician = literal_eval(self.session.vars['not_yet_physician'])
#        if self.round_number>5:
#            new_physician = random.choice(not_yet_physician)
#            for p in self.get_players():
#                if p.id_in_group == 25:
#                    p.id_in_group = new_physician
#                    print(not_yet_physician)
#                    print(new_physician)
#                    not_yet_physician.remove(new_physician)
#                    print(not_yet_physician)
#                    self.session.vars['not_yet_physician'] = repr(not_yet_physician)
#                if p.id_in_group == new_physician:
#                    p.id_in_group = 25

        if self.round_number == 1:
            paying_round = random.randint(5, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round
            self.session.vars['lossaversionchosen'] = random.randint (1, 6)
            self.session.vars['riskaversionchosen'] = random.randint(1, 10)
            #print('set the paying round to', paying_round)
        for p in self.get_players():
            p.riskaversionchosen = self.session.vars['riskaversionchosen']
        for p in self.get_players():
            p.lossaversionchosen = self.session.vars['lossaversionchosen']


class Group (BaseGroup):
    threshold_sick_level = models.StringField (
        choices=['sick', 'sick*', 'sick**', 'sick***','more severe than sick***'])
    decision_threshold_sick_level = models.StringField (
        choices=['sick', 'sick*', 'sick**', 'sick***', 'more severe than sick***'])
 #   painThreshold = models.FloatField(min=0.00, max=4.00)

    visit_or_not = models.BooleanField ()
    # prescribed = models.BooleanField()
    total_visit_fee = models.CurrencyField ()
    thresholdExceedCount = models.IntegerField ()
    thresholdExceedCount2 = models.IntegerField ()
    visit_count = models.IntegerField ()

    total_health_patients = models.FloatField ()
    total_payoff_physician = models.FloatField ()
    id_in_group = Constants.id_in_group
    # pain_eligible = models.FloatField(min=painThreshold, max=400)
    id_visit = models.IntegerField ()
    sell = models.IntegerField()
    buy = models.IntegerField()
    exchange = models.IntegerField()

    def painThreshold(self):
        if self.decision_threshold_sick_level == 'sick':
            return float(0.9)
        elif self.decision_threshold_sick_level == 'sick*':
            return 1.39
        elif self.decision_threshold_sick_level == 'sick**':
            return 1.69
        elif self.decision_threshold_sick_level == 'sick***':
            return 2.49
        elif self.decision_threshold_sick_level == 'more severe than sick***':
            return 3

    def set_payoffs(self):
        players = self.get_players ()
        physician = self.get_player_by_role ('physician')
  #      patient = self.get_player_by_role ('patient {}')
        patient1 = self.get_player_by_role ('patient 1')
        patient2 = self.get_player_by_role ('patient 2')
        patient3 = self.get_player_by_role ('patient 3')
        patient4 = self.get_player_by_role ('patient 4')

#        health_impact = 684.72 * math.log1p (0.66 * self.player.pain() + 0.012 - 1)
#        prescribedPatients = [p for p in players if self.p.pain >= self.group.painThreshold]
        print (patient1.decision)
        print (patient2.decision)
        print (patient3.decision)
        print (patient4.decision)

        if patient1.decision:
            if patient1.pain() >= self.painThreshold():
                patient1.is_prescribed = True
            else:
                patient1.is_prescribed = False
        else:
            patient1.is_prescribed = False

        if patient2.decision:
            if patient2.pain() >= self.painThreshold():
                patient2.is_prescribed = True
            else:
                patient2.is_prescribed = False
        else:
            patient2.is_prescribed = False

        if patient3.decision:
            if patient3.pain() >= self.painThreshold():
                patient3.is_prescribed = True
            else:
                patient3.is_prescribed = False
        else:
            patient3.is_prescribed = False

        if patient4.decision:
            if patient4.pain() >= self.painThreshold():
                patient4.is_prescribed = True
            else:
                patient4.is_prescribed = False

    def painThreshold_history(self):
        return [g.painThreshold for g in self.in_previous_rounds ()]

    def visit_id(self):
        if self.get_player_by_role == {'physician'}:
            if self.group.visit_or_not:
                return {self.player.id_in_group}


class Player (BasePlayer):
    sick = models.StringField (choices=['sick***', 'sick**', 'sick*', 'sick'])
    enjoy = models.StringField (choices=['enjoy***', 'enjoy**', 'enjoy*', 'enjoy'])
    buy = models.BooleanField()
    sell = models.BooleanField()
    health_patient = models.FloatField()
#    pain = models.FloatField()
    #   pain = models.FloatField(min=0, max=400, choices=[x/100 for x in range(0, 400)])
    # id = models.StringField
    #    thresholdDecision_physician = models.FloatField(min=0.00, max=4.00)
    thresholdExceed = models.IntegerField ()
    #     doc="Likert Scale: how likely do you think you can get the prescription (0-7))"
    # )
    # total_health_impact = models.FloatField()
    # result_physician = models.CurrencyField()
    # result_patient = models.CurrencyField()
    health_impact = models.FloatField ()
    is_prescribed = models.BooleanField (
        doc="if threshold amount is exceeded (direct response method)"
    )
    is_prescribed2 = models.BooleanField()  #eventually get the drug in that round
    decision = models.BooleanField (initial=False)  # patient's decision: visit or not
    lossaversionchosen = models.IntegerField()

    LTchoice1 = models.StringField(
        choices=['Accept', 'Reject'],
        label='Lottery 1: if the coin turns up head, then you loss $1; if the coin turns up tails, you win $3.',
        widget=widgets.RadioSelectHorizontal)

    LTchoice2 = models.StringField(
        choices=['Accept', 'Reject'],
        label='Lottery 2: if the coin turns up head, then you loss $1.5; if the coin turns up tails, you win $3.',
        widget=widgets.RadioSelectHorizontal)

    LTchoice3 = models.StringField(
        choices=['Accept', 'Reject'],
        label='Lottery 3: if the coin turns up head, then you loss $2; if the coin turns up tails, you win $3.',
        widget=widgets.RadioSelectHorizontal)

    LTchoice4 = models.StringField(
        choices=['Accept', 'Reject'],
        label='Lottery 4: if the coin turns up head, then you loss $2.5; if the coin turns up tails, you win $3.',
        widget=widgets.RadioSelectHorizontal)

    LTchoice5 = models.StringField(
        choices=['Accept', 'Reject'],
        label='Lottery 5: if the coin turns up head, then you loss $3; if the coin turns up tails, you win $3.',
        widget=widgets.RadioSelectHorizontal)

    LTchoice6 = models.StringField(
        choices=['Accept', 'Reject'],
        label='Lottery 6: if the coin turns up head, then you loss $3.5; if the coin turns up tails, you win $3.',
        widget=widgets.RadioSelectHorizontal)


    HLchoice1 = models.StringField(
        choices=['$1.5 Sure amount', 'Lottery'],
        label='Game 1: The lottery has 10% chance to get $3, 90% chance to get $0.1.',
        widget=widgets.RadioSelectHorizontal)

    HLchoice2 = models.StringField(
        choices=['$1.5 Sure amount', 'Lottery'],
        label='Game 2: The lottery has 20% chance to get $3, 80% chance to get $0.1.',
        widget=widgets.RadioSelectHorizontal)

    HLchoice3 = models.StringField(
        choices=['$1.5 Sure amount', 'Lottery'],
        label='Game 3: The lottery has 30% chance to get $3, 70% chance to get $0.1.',
        widget=widgets.RadioSelectHorizontal)

    HLchoice4 = models.StringField(
        choices=['$1.5 Sure amount', 'Lottery'],
        label='Game 4: The lottery has 40% chance to get $3, 60% chance to get $0.1.',
        widget=widgets.RadioSelectHorizontal)

    HLchoice5 = models.StringField(
        choices=['$1.5 Sure amount', 'Lottery'],
        label='Game 5: The lottery has 50% chance to get $3, 50% chance to get $0.1.',
        widget=widgets.RadioSelectHorizontal)

    HLchoice6 = models.StringField(
        choices=['$1.5 Sure amount', 'Lottery'],
        label='Game 6: The lottery has 60% chance to get $3, 40% chance to get $0.1.',
        widget=widgets.RadioSelectHorizontal)

    HLchoice7 = models.StringField(
        choices=['$1.5 Sure amount', 'Lottery'],
        label='Game 7: The lottery has 70% chance to get $3, 30% chance to get $0.1.',
        widget=widgets.RadioSelectHorizontal)

    HLchoice8 = models.StringField(
        choices=['$1.5 Sure amount', 'Lottery'],
        label='Game 8: The lottery has 80% chance to get $3, 20% chance to get $0.1.',
        widget=widgets.RadioSelectHorizontal)

    HLchoice9 = models.StringField(
        choices=['$1.5 Sure amount', 'Lottery'],
        label='Game 9: The lottery has 90% chance to get $3, 10% chance to get $0.1.',
        widget=widgets.RadioSelectHorizontal)

    HLchoice10 = models.StringField(
        choices=['$1.5 Sure amount', 'Lottery'],
        label='Game 10: The lottery has 100% chance to get $3, 0% chance to get $0.1.',
        widget=widgets.RadioSelectHorizontal)

    riskaversionchosen = models.IntegerField()

    age = models.IntegerField (label='1. What is your age (in years)?', min=18, max=125)

    gender = models.StringField (
        choices=['Male', 'Female', 'Other'],
        label='2. What is your gender?',
        widget=widgets.RadioSelect)

    marriage = models.StringField (
        choices=['Single, Never Married', 'Married, Civil Union, Domestic Partner', 'Separated', 'Divorced', 'Widowed'],
        label='3. What is your marital status?',
        widget=widgets.RadioSelect)

    student = models.StringField (
        choices=['Full-time Student', 'Part-time Student', 'Not a Student'],
        label='4. Are you a full time or part time student?',
        widget=widgets.RadioSelect)

    year = models.StringField (
        choices=['Freshman', 'Sophomore', 'Junior', 'Senior', 'Graduate Student', 'Not a Student'],
        label='5. What is your current student classification?',
        widget=widgets.RadioSelect)

    home_country = models.StringField (
        choices=['United States', 'Another Country'],
        label='6. Where were you born?',
        widget=widgets.RadioSelect)

    language = models.StringField (
        choices=['Yes', 'No'],
        label='7. Do you speak a language other than English at home?',
        widget=widgets.RadioSelect)

    employment = models.StringField (
        choices=['Not Working', 'Temporary Job', 'Permanent Job less than 30 hours per week',
                 'Permanent Job more than 30 hours per week'],
        label='8. What is your employment status?',
        widget=widgets.RadioSelect)

    income = models.StringField (
        choices=['Less than $14,000', '$14,000 - $27,999', '$28,000 - $43,999', '$44,000 - $65,999',
                 '$66,000 - $89,999',
                 '$90,000 or above', 'Not Applicable'],
        label='9. What is your own yearly income?',
        widget=widgets.RadioSelect)

    experiment_experience = models.StringField (
        choices=['Yes', 'No', 'Do not remember'],
        label='10. Have you ever participated in any similar experiment before?',
        widget=widgets.RadioSelect)

    risk = models.StringField(
        choices=['Strongly Disagree', 'Disagree', 'Slightly Disagree', 'Slightly Agree', 'Agree', 'Strongly Agree'],
        label='11. You are the person who is fully prepared to take risks.',
        widget=widgets.RadioSelect)


    decision01 = models.TextField (initial=None, verbose_name="How you made your decisions in Part 1? "
                                                              "Please describe your decision making process as a physician and a patient if you have played both roles in the past 30 rounds. ")
    comments = models.TextField (blank=True, initial=None,
                                 verbose_name="Do you have any comment, questions, or complains about today's experiment?")

    def physician_player(self):
        return self.get_others_in_group ()[25]

    def get_visitor(self):
        if self.player.role == {'physician'}:
            return self.group.visit_or_not.get_others_in_group ()

    def role(self):
        if self.id_in_group == 25:
            return 'physician'
        if self.id_in_group in (1, 2,3,4,5,6,7,8):
            return 'patient 1'
        if self.id_in_group in (9,10,11,12):
            return 'patient 2'
        if self.id_in_group in (13,14,15,16):
            return 'patient 3'
        else:
            return 'patient 4'


    def action(self):
        if self.decision == True:
            return 'visit'
        else:
            return 'not visit'

    def pain(self):
        if self.id_in_group in (1, 2,3,4,5,6,7,8):
            return 0.94
        if self.id_in_group in (9,10,11,12):
            return 1.40
        if self.id_in_group in (13,14,15,16):
            return 1.70
        if self.id_in_group in (17,18,19,20,21,22,23,24):
            return 2.50
        else:
            return 0

    def sick1(self):
        if self.id_in_group in (1,2,3,4,5,6,7,8):
            return 'sick'
        if self.id_in_group in (9,10,11,12):
            return 'sick*'
        if self.id_in_group in (13,14,15,16):
            return 'sick**'
        if self.id_in_group in (17,18,19,20,21,22,23,24):
            return 'sick***'
        else:
            return 0

    def taste(self):
        if self.id_in_group in (1, 2,3,4,5,6,7,8):
            return 1000
        elif self.id_in_group in (9,10,11,12):
            return 165

        elif self.id_in_group in (13,14,15,16):
            return 50

        elif self.id_in_group in (17,18,19,20,21,22,23,24):
            return 250
        else:
            return 'None'

    def taste1(self):
        if self.id_in_group in (1, 2,3,4,5,6,7,8):
            return 'enjoy***'
        if self.id_in_group in (9,10,11,12):
            return 'enjoy*'
        if self.id_in_group in (13,14,15,16):
            return 'enjoy'
        if self.id_in_group in (17,18,19,20,21,22,23,24):
            return 'enjoy**'
        else:
            return 0

    @property
    def patient(self):
        pain = models.FloatField ()
        taste = models.FloatField ()
        id_pain_dic = {self.id_in_group: pain}
        id_taste_dic = {self.id_in_group: taste}

        if self.id_in_group in [1, 2]:
            id_pain_dic[self.id_in_group] = 0.94
            id_taste_dic[self.id_in_group] = 1000
            print ("I am patient self.id_in_group, my pain level k = 0.94, and my taste for opioid is 1000")
            return 'patient with pain level 0.94', 'patient with taste level 1000'
        if self.id_in_group == 3:
            id_pain_dic[self.id_in_group] = 1.4
            id_taste_dic[self.id_in_group] = 165
            print ("I am patient self.id_in_group, my pain level k = 1.4, and my taste for opioid is 165")
            return 'patient with pain level 1.4', 'patient with taste level 165'
        if self.id_in_group == 4:
            id_pain_dic[self.id_in_group] = 1.7
            id_taste_dic[self.id_in_group] = 50
            print ("I am patient self.id_in_group, my pain level k = 1.7, and my taste for opioid is 50")
            return 'patient with pain level 1.7', 'patient with taste level 50'
        if self.id_in_group in [5,6]:
            id_pain_dic[self.id_in_group] = 2.5
            id_taste_dic[self.id_in_group] = 50
            print ("I am patient self.id_in_group, my pain level k = 2.5, and my taste for opioid is 250")
            return 'patient with pain level 2.5', 'patient with taste level 250'

    def pain_threshold(self):
        if self.id_in_group == 25:
            print ("You are a physician with 24 patients and your patient pain level is " +
                   str (Constants.id_pain_dic[self.id_in_group_patient]))
            # return float(input('given the pain level of your patients, enter a threshold pain level:'))

    def result_patient(self):
        if self.id_in_group in (1,2,3,4,5,6,7,8):
            if self.decision:  #visit
                if self.is_prescribed == False:
                    if self.is_prescribed2:
                        return round(653 + 1000 - 103 - 314 - 550,2)
                    else:
                        return round(653 - 103,2)
                else: # get the prescription from the physician
                    if self.sell:
                        return round(653 - 103 - 15 + 550,2)
                    else:   # get it from the physician, consume
                        return round(653 + 1000 - 15 - 103 - 314,2)
            else:
                if self.is_prescribed2:
                    return round(653 -550 +1000 - 314,2)
                else:
                    return round(653,2)

        if self.id_in_group in (9,10,11,12):
            if self.decision:
                if self.is_prescribed == False:
                    if self.is_prescribed2:
                        return round(653 + 165 - 45 - 103 - 550,2)
                    else:
                        return round(653 - 103,2)
                else: # get the prescription from the physician
                    if self.sell:
                        return round(653 - 103 - 15 + 550,2)
                    else:   # get it from the physician, consume
                        return round(653 + 165 - 45 - 15 - 103,2)
            else:
                if self.is_prescribed2:
                    return round(653 - 550 + 165 - 45,2)
                else:
                    return round(653,2)

        if self.id_in_group in (13,14,15,16):
            if self.decision:
                if self.is_prescribed == False:
                    if self.is_prescribed2:
                        return round(653 + 86 + 50 - 103 - 550,2)
                    else:
                        return round(653 - 103,2)
                else:  # get the prescription from the physician
                    if self.sell:
                        return round(653 - 103 - 15 + 550,2)
                    else:  # get it from the physician, consume
                        return round(653 + 86 + 50 - 15 - 103,2)
            else:
                if self.is_prescribed2:
                    return round(653 - 550 + 86 + 50,2)
                else:
                    return round(653,2)

        if self.id_in_group in (17,18,19,20,21,22,23,24):
            if self.decision:
                if self.is_prescribed == False:
                    if self.is_prescribed2:
                        return round(653 + 348 + 250 - 103 - 550,2)
                    else:
                        return round(653 - 103,2)
                else:  # get the prescription from the physician
                    if self.sell:
                        return round(653 - 103 - 15 + 550,2)
                    else:  # get it from the physician, consume
                        return round(653 + 348 + 250 - 15 - 103,2)
            else:
                if self.is_prescribed2:
                    return round(653 - 550 + 348 + 250,2)
                else:
                    return round(653,2)

    def result_patient2(self):
        if self.id_in_group in (1,2,3,4,5,6,7,8):
            if self.decision:  #visit
                if self.is_prescribed == False:
                    if self.is_prescribed2:
                        return round((653 + 1000 - 103 - 314 - 550)/100,0)
                    else:
                        return round((653 - 103)/100, 0)
                else: # get the prescription from the physician
                    if self.sell:
                        return round((653 - 103 - 15 + 550)/100, 0)
                    else:   # get it from the physician, consume
                        return round((653 + 1000 - 15 - 103 - 314)/100,0)
            else:
                if self.is_prescribed2:
                    return round((653 -550 +1000 - 314)/100,0)
                else:
                    return round((653)/100,0)

        if self.id_in_group in (9,10,11,12):
            if self.decision:
                if self.is_prescribed == False: #did not buy from the physician
                    if self.is_prescribed2:
                        return round((653 + 165 - 45 - 103 - 550)/100,0)
                    else:
                        return round((653 - 103)/100,0)
                else: # get the prescription from the physician
                    if self.sell:
                        return round((653 - 103 - 15 + 550)/100,0)
                    else:   # get it from the physician, consume
                        return round((653 + 165 - 45 - 15 - 103)/100,0)
            else:
                if self.is_prescribed2:
                    return round((653- 550 + 165 - 45)/100,0)
                else:
                    return round((653)/100,0)

        if self.id_in_group in (13,14,15,16):
            if self.decision:
                if self.is_prescribed == False:
                    if self.is_prescribed2:#buy
                        return round((653 + 86 + 50 - 103 - 550)/100,0)
                    else:
                        return round((653 - 103)/100,0)
                else:  # get the prescription from the physician
                    if self.sell:
                        return round((653 - 103 - 15 + 550)/100,0)
                    else:  # get it from the physician, consume
                        return round((653 + 86 + 50 - 15 - 103)/100, 0)
            else:
                if self.is_prescribed2:
                    return round((653- 550 + 86 + 50)/100,0)
                else:
                    return round((653/100),0)

        if self.id_in_group in (17,18,19,20,21,22,23,24):
            if self.decision:
                if self.is_prescribed == False:
                    if self.is_prescribed2:
                        return round((653 + 348 + 250 - 103 - 550)/100,0)
                    else:
                        return round((653 - 103)/100,0)
                else:  # get the prescription from the physician
                    if self.sell:
                        return round((653 - 103 - 15 + 550)/100,0)
                    else:  # get it from the physician, consume
                        return round((653 + 348 + 250 - 15 - 103)/100,0)
            else:
                if self.is_prescribed2:
                    return round((653 - 550 + 348 + 250)/100,0)
                else:
                    return round((653)/100,0)

    def result_patient3(self):
        if self.id_in_group in (1,2,3,4,5,6,7,8):
            if self.decision:  #visit
                if self.is_prescribed == False:
                    if self.is_prescribed2:
                        return round((653 + 1000 - 103 - 314 - 550)/100+10, 0)
                    else:
                        return round((653 - 103)/100+10, 0)
                else: # get the prescription from the physician
                    if self.sell:
                        return round((653 - 103 - 15 + 550)/100+10, 0)
                    else:   # get it from the physician, consume
                        return round((653 + 1000 - 15 - 103 - 314)/100+10, 0)
            else:
                if self.is_prescribed2:
                    return round((653 -550 +1000 - 314)/100+10, 0)
                else:
                    return round((653)/100+10, 0)

        if self.id_in_group in (9,10,11,12):
            if self.decision:
                if self.is_prescribed == False:
                    if self.is_prescribed2:
                        return round(((653 + 165 - 45 - 103 - 550)/100)+10, 0)
                    else:
                        return round(((653- 103)/100)+10, 0)
                else: # get the prescription from the physician
                    if self.sell:
                        return round(((653 - 103 - 15 + 550)/100)+10, 0)
                    else:   # get it from the physician, consume
                        return round(((653 + 165 - 45 - 15 - 103)/100)+10, 0)
            else:
                if self.is_prescribed2:
                    return round(((653 - 550 + 165 - 45)/100)+10,0)
                else:
                    return round(((653)/100)+10, 0)

        if self.id_in_group in (13,14,15,16):
            if self.decision:
                if self.is_prescribed == False:
                    if self.is_prescribed2:
                        return round((653 + 86 + 50 - 103 - 550)/100+10, 0)
                    else:
                        return round((653 - 103)/100, 0)+10
                else:  # get the prescription from the physician
                    if self.sell:
                        return round((653 - 103 - 15 + 550)/100+10, 0)
                    else:  # get it from the physician, consume
                        return round((653 + 86 + 50 - 15 - 103)/100, 0)+10
            else:
                if self.is_prescribed2:
                    return round((653 - 550 + 86 + 50)/100+10, 0)
                else:
                    return round((653)/100+10, 0)

        if self.id_in_group in (17,18,19,20,21,22,23,24):
            if self.decision:
                if self.is_prescribed == False:
                    if self.is_prescribed2:
                        return round((653 + 348 + 250 - 103 - 550)/100+10, 0)
                    else:
                        return round((653 - 103)/100+10, 0)
                else:  # get the prescription from the physician
                    if self.sell:
                        return round((653 - 103 - 15 + 550)/100+10, 0)
                    else:  # get it from the physician, consume
                        return round((653 + 348 + 250 - 15 - 103)/100+10, 0)
            else:
                if self.is_prescribed2:
                    return round((653 - 550 + 348 + 250)/100+10, 0)
                else:
                    return round((653/100)+10, 0)

    def total_health_impact(self):
        if self.group.painThreshold() <= 0.94:
            return Constants.weight_factor_health * ((-314) * 8 + (-45) * 4 + 86 * 4 + 348 * 8)

        elif self.group.painThreshold() <= 1.40:
            return Constants.weight_factor_health * ((-45) * 4 + 86 * 4 + 348 * 8)

        elif self.group.painThreshold() <= 1.70:
            return Constants.weight_factor_health * (86 * 4 + 348 * 8)
        elif self.group.painThreshold() <= 2.50:
            return Constants.weight_factor_health * (348 * 8)
        else:
            return 0

    def result_physician(self):
        if self.group.painThreshold() <= 0.94:
            return self.group.total_health_patients + Constants.per_visit_fee * self.group.thresholdExceedCount2

        elif self.group.painThreshold() <= 1.40:
            return self.group.total_health_patients + Constants.per_visit_fee * self.group.thresholdExceedCount2

        elif self.group.painThreshold() <= 1.70:
            return self.group.total_health_patients + Constants.per_visit_fee * self.group.thresholdExceedCount2
        elif self.group.painThreshold() <= 2.50:
            return self.group.total_health_patients + Constants.per_visit_fee * self.group.thresholdExceedCount2

        else:
            return c(0)

    def result_physician2(self):

        if self.group.painThreshold() <= 0.94:
            return round((self.group.total_health_patients + Constants.per_visit_fee * self.group.thresholdExceedCount2) / 100, 0)

        elif self.group.painThreshold() <= 1.40:
            return round ((self.group.total_health_patients + Constants.per_visit_fee * self.group.thresholdExceedCount2) / 100,
                          0)

        elif self.group.painThreshold() <= 1.70:
            return round ((self.group.total_health_patients + Constants.per_visit_fee * self.group.thresholdExceedCount2) / 100,0)
        elif self.group.painThreshold() <= 2.50:
            return round ((self.group.total_health_patients + Constants.per_visit_fee * self.group.thresholdExceedCount2) / 100, 0)

        else:
            return round (c (0) / 100, 0)


def health_function(k_i):
    return 684.72 * math.log1p (0.66 * k_i + 0.012 - 1)


def sum(health_impact):
    z = 0
    for k_i in models.group.pain_eligible:
        z = z + 684.72 * math.log1p (0.66 * k_i + 0.012 - 1)
        return z



