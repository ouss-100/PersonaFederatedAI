"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
var client_1 = require("@prisma/client");
var prisma = new client_1.PrismaClient();
// Function to generate random percentages summing to 100 for the five personalities
function generatePersonalityValues() {
    // Generate random values for 5 personalities
    var value1 = Math.random() * 100;
    var value2 = Math.random() * (100 - value1);
    var value3 = Math.random() * (100 - value1 - value2);
    var value4 = Math.random() * (100 - value1 - value2 - value3);
    var value5 = 100 - (value1 + value2 + value3 + value4);
    // Shuffle the values to make them random
    var values = [value1, value2, value3, value4, value5];
    values.sort(function () { return Math.random() - 0.5; });
    return [
        { name: "Openness", value: values[0] },
        { name: "Conscientiousness", value: values[1] },
        { name: "Agreeableness", value: values[2] },
        { name: "Extraversion", value: values[3] },
        { name: "Neuroticism", value: values[4] },
    ];
}
// Dummy user data
var users = [
    {
        email: "med.mouhib@example.com",
        name: "Med Mouhib",
        dominantpersonality: "Extraversion",
    },
    {
        email: "sofia.karoui@example.com",
        name: "Sofia Karoui",
        dominantpersonality: "Openness",
    },
    {
        email: "ali.benhassen@example.com",
        name: "Ali Ben Hassen",
        dominantpersonality: "Conscientiousness",
    },
    {
        email: "amira.chaouachi@example.com",
        name: "Amira Chaouachi",
        dominantpersonality: "Agreeableness",
    },
    {
        email: "khaled.zied@example.com",
        name: "Khaled Zied",
        dominantpersonality: "Neuroticism",
    },
];
function seed() {
    return __awaiter(this, void 0, void 0, function () {
        var _i, users_1, userData, personalities, user, error_1;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 5, 6, 8]);
                    _i = 0, users_1 = users;
                    _a.label = 1;
                case 1:
                    if (!(_i < users_1.length)) return [3 /*break*/, 4];
                    userData = users_1[_i];
                    personalities = generatePersonalityValues();
                    return [4 /*yield*/, prisma.user.create({
                            data: {
                                email: userData.email,
                                name: userData.name,
                                dominantpersonality: userData.dominantpersonality,
                                userpersonality: {
                                    create: personalities.map(function (personality) { return ({
                                        name: personality.name,
                                        value: personality.value,
                                    }); }),
                                },
                            },
                        })];
                case 2:
                    user = _a.sent();
                    console.log("User created: ".concat(user.name, " (ID: ").concat(user.id, ")"));
                    _a.label = 3;
                case 3:
                    _i++;
                    return [3 /*break*/, 1];
                case 4: return [3 /*break*/, 8];
                case 5:
                    error_1 = _a.sent();
                    console.error("Error seeding database:", error_1);
                    return [3 /*break*/, 8];
                case 6: return [4 /*yield*/, prisma.$disconnect()];
                case 7:
                    _a.sent();
                    return [7 /*endfinally*/];
                case 8: return [2 /*return*/];
            }
        });
    });
}
seed();
