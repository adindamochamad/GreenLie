import { NextResponse } from "next/server";
import { VERSI_API } from "@/lib/greenlie/layanan";

export async function GET() {
  return NextResponse.json({ status: "ok", version: VERSI_API });
}
