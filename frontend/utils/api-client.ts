import { EnvVars } from "@/env";
import axios from "axios";

console.log("api_url"+EnvVars.API_URL)
export const apiClient = axios.create({ baseURL: EnvVars.API_URL })