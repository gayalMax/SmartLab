/**
 * Initial state of the admin labs state
 */
const initialState = {
  attributes: [],
  itemsets: [],

  syncedItemsets: [],

  createItemsetError: null,
  createItemsetLoading: false,
  createItemsetSuccess: null,

  itemSetsSyncLoading: false,
  itemSetsSyncSuccess: null,
  itemSetsSyncError: null
};

export default initialState;
