import Vue from 'vue'
import Router from 'vue-router'
import MemoriesList from "../components/MemoriesList";
import MemoryForm from "../components/MemoryForm";


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/list',
      name: 'memories',
      component: MemoriesList
    },
    {
      path: '/memory/new',
      name: 'new-memory',
      component: MemoryForm
    }
  ]
})
