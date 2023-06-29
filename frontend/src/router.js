import { createWebHistory, createRouter} from 'vue-router'

import OverviewDashboardView from "@/views/OverviewDashboardView.vue";
import LoginView from "@/views/LoginView.vue";
import ManageGroupsView from "@/views/ManageGroupsView.vue";

const routes = [
    {
        path: '/overview',
        name: 'overview-dashboard',
        component: OverviewDashboardView,
    },
    {
        path: '/',
        name: 'login',
        component: LoginView,
    },
    {
        path: '/groups',
        name: 'groups-manager',
        component: ManageGroupsView,
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router