<?php

namespace App\Controller;

use App\Entity\BonusesUser;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use App\Entity\User;
use App\Entity\Campaigns;

class AdminFunctionalController extends AbstractController
{
    /**
     * @Route("/admin/functional", name="admin_functional")
     */
    public function index(): Response
    {
        return $this->render('admin_functional/index.html.twig', [
            'controller_name' => 'AdminFunctionalController',
        ]);
    }

    /**
     * @Route("/admin/delete_user/{id}", name="admin_delete")
     */
    public function delete(int $id): Response
    {
        $user = $this->getDoctrine()->getRepository(User::class)->find($id);
        $entityManager = $this->getDoctrine()->getManager();
        $entityManager->remove($user);
        $entityManager->flush();
        return $this->redirectToRoute('admin');
    }

    /**
     * @Route("/admin/rights_admin/{id}", name="admin_make")
     */
    public function make_admin(int $id): Response
    {
        $user = $this->getDoctrine()->getRepository(User::class)->find($id);
        $user->setRoles(['ROLE_ADMIN']);
        $entityManager = $this->getDoctrine()->getManager();
        $entityManager->persist($user);
        $entityManager->flush();
        return $this->redirectToRoute('admin');
    }

    /**
     * @Route("/admin/rights_user/{id}", name="admin_user_make")
     */
    public function make_user(int $id): Response
    {
        $user = $this->getDoctrine()->getRepository(User::class)->find($id);
        $user->setRoles(['ROLE_USER']);
        $entityManager = $this->getDoctrine()->getManager();
        $entityManager->persist($user);
        $entityManager->flush();
        return $this->redirectToRoute('admin');
    }

}
