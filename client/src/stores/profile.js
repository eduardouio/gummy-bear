import { defineStore } from "pinia";

export default defineStore("profile", {
    state: () => ({
        profile: null,
        status: null,
    }),
    actions: {
        setProfile(profile) {
            this.profile = profile;
        },
    },
});