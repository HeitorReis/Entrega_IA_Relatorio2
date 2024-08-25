import pandas as pd

class GroupedAttDataset:
    
    def __init__( self ):
        self.users = list()
        self.dframe = pd.DataFrame()
    
    def add_user_from_scratch( self, new_user: list ): # Add a single user to the grouped dataset
        
        if not new_user:
            return print('An empty user tried to be added.')
        
        grouped_user = self.group(new_user) # Group itemsets into new itemsets
        
        self.users.append(grouped_user) # Add to the list
    
    def group( self, new_user: list ): # Group the attributes from a user
    
        grouped_user = set()
        
        for itemset in new_user:
        
            if itemset[0].isnumeric():
                grouped_user.add(itemset)
            
            else:
                for key, att in group_map.items():
                    
                    if type(att) != type(list()):
                        
                        if att in itemset:
                            grouped_user.add(str(key))
                    
                    else:
                        for this_code in att:
                            
                            if this_code in itemset:
                                grouped_user.add(str(key))
        
        return list(grouped_user)
    
    def add_user_list_from_scratch( self, new_user_list ):
        
        for new_user in new_user_list: # For every user, add it from scratch
            self.add_user_from_scratch( new_user )
    
    def commit_dataframe( self ):
        import pandas as pd

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





group_map = {
            'Tem_Instr_Inundacao': [
                'Mgrd181', 'Mgrd182', 'Mgrd183',
                'Mgrd184', 'Mgrd185', 'Mgrd186',
                'Mgrd187', 'Mgrd171', 'Mgrd172', 'Mgrd173'
                ],
            'Nao_Instr_Inundacao': ['Mgrd188'],
            'Tem_Instr_Deslizamento': [
                'Mgrd201', 'Mgrd202', 'Mgrd203',
                'Mgrd204', 'Mgrd205', 'Mgrd206',
                'Mgrd207', 'Mgrd174', 'Mgrd175', 'Mgrd176'
                ],
            'Nao_Instr_Deslizamento': ['Mgrd208'],
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
            'Nao_Medida_Estrutural_RRD': ['Mgrd2215'],
            'Tem_Atv_P&DC': [
                'Mgrd231', 'Mgrd232', 'Mgrd233',
                'Mgrd234', 'Mgrd235', 'Mgrd236',
                'Mgrd237', 'Mgrd238'
            ],
            'Nao_ATV_P&DC': 'Mgrd239',
            'Tem_Red_Seca': [
                'Mgrd041', 'Mgrd042', 'Mgrd043',
                'Mgrd044', 'Mgrd045', 'Mgrd046',
                'Mgrd047', 'Mgrd048', 'Mgrd05', 'Mgrd049'
            ],
            'Nao_RR_Seca': 'Mgrd0410',
            'Atingido_Seca': 'Mgrd01',
            #'Ano_Seca': 'Mgrd02',
            'Atingido_Alagamentos': 'Mgrd06',
            #'Ano_Alagamento': 'Mgrd07',
            'Atingido_Enchente': 'Mgrd08',
            #'Ano_Enchente': 'Mgrd09',
            'Tem_Red_Enchente': [
                'Mgrd1051', 'Mgrd1052', 'Mgrd1053',
                'Mgrd1054', 'Mgrd1055', 'Mgrd1056',
                'Mgrd1057', 'Mgrd1058', 'Mgrd1059',
                'Mgrd10510', 'Mgrd181', 'Mgrd184',
                'Mgrd186', 'Mgrd187', 'Mgrd171',
                'Mgrd172', 'Mgrd173'
            ],
            'Nao_Red_Enchente': ['Mgrd10512', 'Mgrd10511'],
            'Atingido_Enxurrada': ['Mgrd11'],
            #'Ano_Enxurrada': ['Mgrd12'],
            'Tem_Red_Enxurrada': [
                'Mgrd1351', 'Mgrd1352', 'Mgrd1353',
                'Mgrd1354', 'Mgrd1355', 'Mgrd1356',
                'Mgrd1357', 'Mgrd1358', 'Mgrd1359',
                'Mgrd13510', 'Mgrd181', 'Mgrd184',
                'Mgrd186', 'Mgrd187', 'Mgrd171',
                'Mgrd172', 'Mgrd173'
            ],
            'Nao_Red_Enxurrada': ['Mgrd13512', 'Mgrd13511'],
            'Tem_Red_Enc_Enx': [
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
            'Tem_Red_Des': [
                'Mgrd1651', 'Mgrd1652', 'Mgrd1653',
                'Mgrd1654', 'Mgrd1655', 'Mgrd1656',
                'Mgrd1657', 'Mgrd201', 'Mgrd207',
                'Mgrd206', 'Mgrd204', 'Mgrd174',
                'Mgrd175', 'Mgrd176'
            ],
            'Nao_Red_Des': ['Mgrd1659', 'Mgrd1658'],
        }