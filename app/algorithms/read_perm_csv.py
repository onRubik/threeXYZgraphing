

def read_perm_csv(origin, out_pd_read, node_history):
    try:

        filter1 = out_pd_read['id1'] == origin
        new_set = out_pd_read.where(filter1)
        new_source = new_set[~new_set['id2'].isin(node_history)]
        nearest_node = new_source['distance'].min()
        nearest_node_filter = new_source['distance'] == nearest_node
        filter2_arg = out_pd_read.where(nearest_node_filter)
        filter_not_null = filter2_arg.notnull()
        i_next_node = filter_not_null[filter_not_null['id1'] == True].index.tolist()[0]
        result_min = out_pd_read.iat[i_next_node, 1]
        
        return result_min

    except Exception as e:
        print(e)


if __name__ == '__main__':
    read_perm_csv()