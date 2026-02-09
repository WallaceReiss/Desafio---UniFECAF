import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Testa o endpoint de health check"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "unifecaf-api"}

def test_login():
    """Testa o endpoint de login"""
    response = client.post("/auth/login")
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_dashboard_without_token():
    """Testa acesso ao dashboard sem token"""
    response = client.get("/dashboard/")
    assert response.status_code == 401

def test_dashboard_with_token():
    """Testa acesso ao dashboard com token válido"""
    # Primeiro pega o token
    login_response = client.post("/auth/login")
    token = login_response.json()["access_token"]
    
    # Depois acessa o dashboard
    response = client.get(
        "/dashboard/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    
    # Valida estrutura da resposta
    assert "student" in data
    assert "today_classes" in data
    assert "notifications" in data
    assert "academic_summary" in data
    assert "financial_summary" in data
    
    # Valida dados do estudante
    assert data["student"]["name"] == "Candidato(a) Pleno Teste"
    assert data["student"]["ra"] == "20240988"
    assert data["student"]["total_progress"] == 45

def test_dashboard_data_structure():
    """Testa a estrutura completa dos dados do dashboard"""
    login_response = client.post("/auth/login")
    token = login_response.json()["access_token"]
    
    response = client.get(
        "/dashboard/",
        headers={"Authorization": f"Bearer {token}"}
    )
    data = response.json()
    
    # Valida academic_summary
    assert len(data["academic_summary"]) == 2
    assert data["academic_summary"][0]["subject"] == "Desenvolvimento Web Fullstack"
    assert data["academic_summary"][0]["grade"] == 8.5
    assert data["academic_summary"][0]["absences"] == 12
    
    # Valida financial_summary
    assert data["financial_summary"]["status"] == "PENDING"
    assert data["financial_summary"]["value"] == 450.00
    
    # Valida notifications
    assert len(data["notifications"]) == 2
    assert data["notifications"][0]["read"] == False
    assert data["notifications"][1]["read"] == True
