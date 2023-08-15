import { createWebHistory, createRouter} from 'vue-router'

import {useAuthStore} from "@/store";

import OverviewDashboardView from "@/views/OverviewDashboardView.vue";
import LoginView from "@/views/LoginView.vue";
import ManageGroupsView from "@/views/ManageGroupsView.vue";

const routes = [
    {
        path: '/overview',
        name: 'overview-dashboard',
        component: OverviewDashboardView,
        meta: {requiresAuth: true},
    },
    {
        path: '/',
        name: 'login',
        component: LoginView,
        meta: {requiresAuth: false},
    },
    {
        path: '/groups',
        name: 'groups-manager',
        component: ManageGroupsView,
        meta: {requiresAuth: true},
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
    const authStore = useAuthStore();

    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!authStore.is_authenticated) {
            next({name: 'login'});
        } else {
            next();
        }
    } else {
        next();
    }
});

export default router;