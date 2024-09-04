import pandas as pd

class GroupedAttDataset:
    
    def __init__( self ):
        self.users = list()
        self.dframe = pd.DataFrame()
    
    
    def add_user_from_scratch( self, new_user: list ): # Add a single user to the grouped dataset
        
        grouped_user = self.group(new_user) # Group itemsets into new itemsets
        
        self.users.append(grouped_user) # Add to the list
    
    
    def group( self, new_user: list ): # Group the attributes from a user
    
        grouped_user = set()
        
        for item in new_user[0:2]:
            grouped_user.add(item)
        
        for itemset in new_user:
            
            for key, att in group_map.items():
                
                if type(att) != type(list()):
                    
                    if att in itemset:
                        grouped_user.add(str(key))
                
                else:
                    for this_code in att:
                        
                        if this_code in itemset:
                            grouped_user.add(str(key))
        
        occurrences = []
        for index, group in enumerate(group_map.keys()):
            if group in grouped_user:
                occurrences.append(True)
            else:
                occurrences.append(False)
        
        for group_index, group_name in enumerate(group_map.keys()):
            group_exist = occurrences[group_index]
            if (not group_exist) and ('Nao' not in group_name) and ('Nao_'+group_name not in grouped_user):
                grouped_user.add('Nao_'+str(group_name))
        
        return sorted(list(grouped_user))
    
    
    def add_user_list_from_scratch( self, new_user_list ):
        
        for new_user in new_user_list: # For every user, add it from scratch
            self.add_user_from_scratch( new_user )
    
    
    def commit_dataframe( self ):
        
        # Lists of occurrences = gad
        list_of_lists = self.users[:]

        # Combine all lists into a single list
        all_events = [item for sublist in list_of_lists for item in sublist]

        # Get unique events
        unique_events = sorted(set(all_events))

        # Create a dictionary to hold occurrences
        data = []

        for event_list in list_of_lists:
            row = {event: 1 if event in event_list else 0 for event in unique_events}
            data.append(row)

        # Convert the dictionary into a DataFrame
        self.dframe = pd.DataFrame(data, columns=unique_events)
    
    
    def filter_dframe ( self , gradient: float): # Removes the columns that have support higher than the limit
        for column in self.dframe:
            column_support = (self.dframe[column].sum() / len(self.dframe[column]))
            if column_support > gradient:
                self.dframe.drop(column, axis='columns', inplace=True)
    
    
    def commit_users( self ): # Commit the users according to the dataframe
        
        new_user_list = []
        
        for user_index, new_user in enumerate(self.dframe.values):
            
            new_user_list.append(list())
            
            for value_index, value in enumerate(new_user):
                
                if value == 1:
                    
                    new_user_list[user_index].append(self.dframe.columns[value_index])
        
        self.users = new_user_list





group_map = {
            'Tem_Instr_Inundacao': [
                'Mgrd181', 'Mgrd182', 'Mgrd183',
                'Mgrd184', 'Mgrd185', 'Mgrd186',
                'Mgrd187', 'Mgrd171', 'Mgrd172', 'Mgrd173'
                ],
            'Nao_Tem_Instr_Inundacao': ['Mgrd188'],
            'Tem_Instr_Deslizamento': [
                'Mgrd201', 'Mgrd202', 'Mgrd203',
                'Mgrd204', 'Mgrd205', 'Mgrd206',
                'Mgrd207', 'Mgrd174', 'Mgrd175', 'Mgrd176'
                ],
            'Nao_Tem_Instr_Deslizamento': ['Mgrd208'],
            'Tem_Instr_Municipais': [
                'Mgrd177', 'Mgrd178', 'Mgrd179', 'Mgrd1710'
                ],
            'Tem_Orgs_RRD': [
                'Mgrd211', 'Mgrd212', 'Mgrd213',
                'Mgrd214', 'Mgrd215'
                ],
            'Tem_Medida_Estrutural_RRD': [
                'Mgrd221', 'Mgrd222', 'Mgrd223',
                'Mgrd224', 'Mgrd225', 'Mgrd226',
                'Mgrd227', 'Mgrd228', 'Mgrd229',
                'Mgrd2210', 'Mgrd2211', 'Mgrd2212',
                'Mgrd2213', 'Mgrd2214'
            ],
            'Nao_Tem_Medida_Estrutural_RRD': ['Mgrd2215'],
            'ATV_P&DC': [
                'Mgrd231', 'Mgrd232', 'Mgrd233',
                'Mgrd234', 'Mgrd235', 'Mgrd236',
                'Mgrd237', 'Mgrd238'
            ],
            'Nao_ATV_P&DC': 'Mgrd239',
            'Tem_RR_Seca': [
                'Mgrd041', 'Mgrd042', 'Mgrd043',
                'Mgrd044', 'Mgrd045', 'Mgrd046',
                'Mgrd047', 'Mgrd048', 'Mgrd05', 'Mgrd049'
            ],
            'Nao_Tem_RR_Seca': 'Mgrd0410',
            'Atingido_Seca': 'Mgrd01',
            #'Ano_Seca': 'Mgrd02',
            'Atingido_Alagamentos': 'Mgrd06',
            #'Ano_Alagamento': 'Mgrd07',
            'Atingido_Enchente': 'Mgrd08',
            #'Ano_Enchente': 'Mgrd09',
            'Tem_RR_Enchente': [
                'Mgrd1051', 'Mgrd1052', 'Mgrd1053',
                'Mgrd1054', 'Mgrd1055', 'Mgrd1056',
                'Mgrd1057', 'Mgrd1058', 'Mgrd1059',
                'Mgrd10510', 'Mgrd181', 'Mgrd184',
                'Mgrd186', 'Mgrd187', 'Mgrd171',
                'Mgrd172', 'Mgrd173'
            ],
            'Nao_Tem_RR_Enchente': ['Mgrd10512', 'Mgrd10511'],
            'Atingido_Enxurrada': ['Mgrd11'],
            #'Ano_Enxurrada': ['Mgrd12'],
            'Tem_RR_Enxurrada': [
                'Mgrd1351', 'Mgrd1352', 'Mgrd1353',
                'Mgrd1354', 'Mgrd1355', 'Mgrd1356',
                'Mgrd1357', 'Mgrd1358', 'Mgrd1359',
                'Mgrd13510', 'Mgrd181', 'Mgrd184',
                'Mgrd186', 'Mgrd187', 'Mgrd171',
                'Mgrd172', 'Mgrd173'
            ],
            'Nao_Tem_RR_Enxurrada': ['Mgrd13512', 'Mgrd13511'],
            'Tem_RR_Enc_Enx': [
                'Mgrd1351', 'Mgrd1352', 'Mgrd1353',
                'Mgrd1354', 'Mgrd1355', 'Mgrd1356',
                'Mgrd1357', 'Mgrd1358', 'Mgrd1359',
                'Mgrd13510', 'Mgrd181', 'Mgrd184',
                'Mgrd186', 'Mgrd187', 'Mgrd171',
                'Mgrd172', 'Mgrd173', 'Mgrd10510',
                'Mgrd1051', 'Mgrd1052', 'Mgrd1053',
                'Mgrd1054', 'Mgrd1055', 'Mgrd1056',
                'Mgrd1057', 'Mgrd1058', 'Mgrd1059'
            ],
            'Atingido_Des': ['Mgrd14'],
            #'Ano_Des': ['Mgrd15'],
            'Tem_RR_Des': [
                'Mgrd1651', 'Mgrd1652', 'Mgrd1653',
                'Mgrd1654', 'Mgrd1655', 'Mgrd1656',
                'Mgrd1657', 'Mgrd201', 'Mgrd207',
                'Mgrd206', 'Mgrd204', 'Mgrd174',
                'Mgrd175', 'Mgrd176'
            ],
            'Nao_Tem_RR_Des': ['Mgrd1659', 'Mgrd1658'],
        }